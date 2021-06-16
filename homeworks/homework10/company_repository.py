import aiohttp

import asyncio
import string

from bs4 import BeautifulSoup


class CompanyRepository:
    def __init__(self, url="https://markets.businessinsider.com"):
        self._common_lists_of_companies_pages = []
        self._cache = []
        self._url = url

        self.urls = [
            f"""{self._url}/index/components/s&p_500?p={p}""" for p in range(1, 11)
        ]

    @staticmethod
    async def _parse_company_list(page_with_table):
        soup = BeautifulSoup(page_with_table, "lxml")

        # TODO: check columns names

        table_rows = (
            soup.find("div", {"class": "table-responsive"})
            .find("tbody", {"class": "table__tbody"})
            .find_all("tr")
        )

        for row in table_rows:
            name = row.find("td", {"class": "table__td table__td--big"}).find("a").text
            link = "https://markets.businessinsider.com" + row.find("a").get("href")
            growth = row.find_all("td")[7].text.split()[1]

            company_page = await CompanyRepository._fetch(link)

            yield {
                "Name": name,
                "url": link,
                "Growth": growth,
                **CompanyRepository._parse_company_page(company_page),
            }

    @staticmethod
    def _parse_company_page(page):
        soup = BeautifulSoup(page, "lxml")

        price = soup.find("span", {"class": "price-section__current-value"}).text
        code = (
            soup.find("span", {"class": "price-section__category"})
            .find("span")
            .text.translate(str.maketrans("", "", string.punctuation))
            .strip()
        )

        right_side_of_page = soup.find(
            "div", {"class": "site-content__col site-content__col--right"}
        ).find_all("div", {"class": "snapshot__data-item"})
        table = {
            item.find("div").text: float(item.text.strip().split()[0])
            for item in right_side_of_page
        }

        pne = table["P/E Ratio"]
        week52low = table["52 Week Low"]
        week52high = table["52 Week High"]

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

    async def get_all_companies(self):
        if self._cache:
            for item in self._cache:
                yield item
        else:
            # create a list of tasks to execute
            # get_data_page(page_number) for page_number in range(10)
            for url in self.urls:
                self._common_lists_of_companies_pages.append(await self._fetch(url))

        for list_page in self._common_lists_of_companies_pages:
            # TODO: use yield from
            async for company_blob in self._parse_company_list(list_page):
                yield company_blob
                # company = await Company.from_blob(company_blob)
                # yield company
                # self._cache.append(company)


async def foo():
    repo = CompanyRepository()
    async for company in repo.get_all_companies():
        print(company)
    await asyncio.sleep(10)


asyncio.run(foo())
print("finish")
