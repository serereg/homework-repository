import asyncio
import math
import string
from concurrent.futures import ProcessPoolExecutor

# from decimal import Decimal
from re import sub
from typing import Tuple

import aiohttp
from bs4 import BeautifulSoup

from .company import Company


class CompanyRepository:
    """A class for parsing URL for statistic data."""

    def __init__(self, url="https://markets.businessinsider.com"):
        self._common_lists_of_companies_pages = set()
        self._cache = []
        self._url = url

        self._urls = [
            f"""{self._url}/index/components/s&p_500?p={p}""" for p in range(1, 11)
        ]

    async def _parse_company_list(self, page_with_table: str):
        """Parse one of several pages with list of companies

        Args:
            page_with_table: page source

        Returns:
            Blob with main parameters of company, i.e.
                Name, URL, Growth, Price, Code "P/E Ratio",
                "52 Week Low", "52 Week High".
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

        async def get_comp_page(company_name: str, company_url: str) -> Tuple[str, str]:
            return company_name, await self._fetch_company(company_url)

        tasks = [
            get_comp_page(company_name, additional_info[company_name]["URL"])
            for company_name in additional_info
        ]

        names_and_pages = await asyncio.gather(*tasks)

        with ProcessPoolExecutor(max_workers=len(names_and_pages)) as pool:
            # can't use lambda in pool.map. Don't know the reason
            blobs = pool.map(
                self._get_company_info,
                names_and_pages,
            )

        for name, parsed_page in blobs:
            yield {
                "Name": name,
                "URL": additional_info[name]["URL"],
                "Growth": additional_info[name]["Growth"],
                **parsed_page,
            }

    @classmethod
    def _get_company_info(cls, names_and_pages):
        return names_and_pages[0], cls._parse_company_page(names_and_pages[1])

    @staticmethod
    def _parse_company_page(page):
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

    @staticmethod
    async def _fetch(url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise ValueError(f"Can't open url: {url}")
                return await resp.text()

    @classmethod
    async def _fetch_company(cls, url: str):
        """Mock in easy way of _fetch method"""
        return await cls._fetch(url)

    @classmethod
    async def _fetch_company_list(cls, url: str):
        """Mock in easy way of _fetch method"""
        return await cls._fetch(url)

    async def get_all_companies(self):
        """Return object of class Company."""
        if self._cache:
            for item in self._cache:
                yield item
        else:
            tasks = [self._fetch_company_list(url) for url in self._urls]
            # TODO: remove set. Now it is used to simplify testing
            #  where I can pass less urls
            self._common_lists_of_companies_pages = set(await asyncio.gather(*tasks))

        for list_page in self._common_lists_of_companies_pages:
            # TODO: use yield from
            async for company_blob in self._parse_company_list(list_page):
                # yield company_blob
                company = Company.from_blob(company_blob)
                yield company
                self._cache.append(company)
