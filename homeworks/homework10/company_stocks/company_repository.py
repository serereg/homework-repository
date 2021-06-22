import asyncio
import logging
import math
import string
from concurrent.futures import ProcessPoolExecutor
from re import sub
from typing import Any, Dict, Generator, List

import aiohttp
from bs4 import BeautifulSoup

from .company import Company


class CompanyRepository:
    """A class for parsing URL for statistic data.

    URL for parsing is https://markets.businessinsider.com.

    Todo:
        1. Convert to use generator in right way.
        2. Split class in two subclasses with functional
            of fetch and parsing
    """

    def __init__(self, url="https://markets.businessinsider.com"):
        logging.basicConfig(format="%(asctime)s %(message)s")
        self._cache = []
        self._url = url

    @staticmethod
    async def _fetch(session: aiohttp.ClientSession, url: str) -> str:
        """Fetch page from given url and opened session."""
        async with session.get(url) as resp:
            if resp.status != 200:
                raise ValueError(f"Can't open url: {url}")
            return await resp.text()

    async def _get_all_detailed_pages(self, name_and_short_info: Dict[str, Dict]):
        """Return list of pages for each company."""
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._fetch(session, info[1]["URL"])
                for info in name_and_short_info.items()
            ]
            return await asyncio.gather(*tasks)

    async def _get_all_table_pages(self):
        """Return a list of pages with tables of companies."""
        urls = [
            f"https://markets.businessinsider.com/index/components/s&p_500?p={p}"
            for p in range(1, 11)
        ]
        async with aiohttp.ClientSession() as session:
            tasks = [self._fetch(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    def _parse_table(self, page_with_table: str) -> Dict[str, Dict]:
        """Parse one of several pages with list of companies

        Args:
            page_with_table: page source

        Returns:
             list of companies and it's URLs
        """
        soup = BeautifulSoup(page_with_table, "lxml")

        # TODO: check columns names

        table_rows = (
            soup.find("div", {"class": "table-responsive"})
            .find("tbody", {"class": "table__tbody"})
            .find_all("tr")
        )

        additional_info = {}
        for row in table_rows:
            name = row.find("td", {"class": "table__td table__td--big"}).find("a").text
            link = self._url + row.find("a").get("href")
            growth = float(sub(r"[^\d.]", "", row.find_all("td")[7].text.split()[1]))

            additional_info[name] = {
                "URL": link,
                "Growth": growth,
            }
        return additional_info

    def _parse_pages_with_tables(self, pages: List[str]) -> Dict[str, Any]:
        with ProcessPoolExecutor() as pool:
            list_of_sublists_with_companies = pool.map(self._parse_table, pages)
        name_and_short_info = {}
        for i in list_of_sublists_with_companies:
            name_and_short_info.update(i)
        return name_and_short_info

    @staticmethod
    def _parse_company_page(page: str) -> Dict[str, Any]:
        soup = BeautifulSoup(page, "lxml")

        price = soup.find("span", {"class": "price-section__current-value"}).text
        price = float(sub(r"[^\d.]", "", price))
        code = (
            soup.find("span", {"class": "price-section__category"})
            .find("span")
            .text.translate(str.maketrans("", "", string.punctuation))
            .strip()
        )

        right_side_of_page = soup.find(
            "div", {"class": "site-content__col site-content__col--right"}
        ).find_all("div", {"class": "snapshot__data-item"})
        try:
            table = {
                item.find("div").text.strip(): float(item.text.strip().split()[0])
                for item in right_side_of_page
            }
        except ValueError:
            table = {}
        pne = table.get("P/E Ratio", math.nan)
        week52low = table.get("52 Week Low", math.nan)
        week52high = table.get("52 Week High", math.nan)
        return {
            "Price": price,
            "Code": code,
            "P/E Ratio": pne,
            "52 Week Low": week52low,
            "52 Week High": week52high,
        }

    def _parse_detailed_info(self, pages: List[str]):
        with ProcessPoolExecutor() as pool:
            blobs = pool.map(self._parse_company_page, pages)

        logging.warning("parsing done")
        return list(blobs)

    def _merge_extra_info(self, blobs, names_and_additional_info: Dict[str, Any]):
        for i, name in enumerate(names_and_additional_info):
            yield {
                "Name": name,
                "URL": names_and_additional_info[name]["URL"],
                "Growth": names_and_additional_info[name]["Growth"],
                **blobs[i],
            }

    def get_all_companies(self) -> Generator[Company, None, None]:
        """Return object of class Company."""
        if self._cache:
            for item in self._cache:
                yield item
        else:
            logging.warning("getting all tables with companies")
            table_pages = asyncio.run(self._get_all_table_pages())

            logging.warning("parsing all tables")
            all_companies_short_infos = self._parse_pages_with_tables(table_pages)

            logging.warning("getting all company pages")
            detailed_pages = asyncio.run(
                self._get_all_detailed_pages(all_companies_short_infos)
            )
            logging.warning("parsing all company pages")

            blobs_thin = self._parse_detailed_info(detailed_pages)
            blobs_full = self._merge_extra_info(blobs_thin, all_companies_short_infos)

            for company_blob in blobs_full:
                company = Company.from_blob(company_blob)
                yield company
                self._cache.append(company)
