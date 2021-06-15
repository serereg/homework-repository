import string

import aiohttp
import asyncio

from bs4 import BeautifulSoup
from typing import List


async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise ValueError(f"Can't open url: {url}")
            return await resp.text()


async def fetch_urls(urls: List[str], src_list: list):
    for url in urls:
        src_list.append(await fetch(url))


pages_src: List[str] = []

# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_url1(
# "http://pargolovo.hopto.org", page_src))
#
# soup = BeautifulSoup(page_src[0], "lxml")
#
# li = soup.find_all("meta")
# print(li)

# Businessinsider.com

MAIN_URL = "https://markets.businessinsider.com"
urls = [
    f"""https://markets.businessinsider.com/index/components/s&p_500?p={p}"""
    for p in range(1, 11)
]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_urls(urls, pages_src))


class Company:
    def __init__(self, name: str, url: str):
        self.name = name
        self.profit = 0
        self.loss = 0
        self.price = 0
        self._url = url
        self._blob = ""
        self.code = ""
        self.pne_ratio = 0

    @classmethod
    def from_blob(cls, data):
        soup = BeautifulSoup(data, "lxml")
        company = Company("", "")
        company.price = soup.find(
            "span", {"class": "price-section__current-value"}
        ).text
        company.code = (
            soup.find("span", {"class": "price-section__category"})
            .find("span")
            .text.translate(str.maketrans("", "", string.punctuation))
            .strip()
        )
        items = soup.find(
            "div", {"class": "site-content__col site-content__col--right"}
        ).find_all("div", {"class": "snapshot__data-item"})
        right_table = {
            item.find("div").text: float(item.text.strip().split()[0]) for item in items
        }

        company.pne_ratio = right_table["P/E Ratio"]
        return company

    @property
    def url(self):
        return self._url


def parse_list_of_companies(pages_src):
    companies = {}
    for page in pages_src:
        soup = BeautifulSoup(page, "lxml")

        li = soup.find_all("td", {"class": "table__td table__td--big"})
        for i in li:
            name = i.find("a").text
            link = MAIN_URL + i.find("a").get("href")
            companies[name] = link
    return companies


companies = parse_list_of_companies(pages_src)
print(companies)
print(len(companies))


data = ""


url = "https://markets.businessinsider.com/stocks/amat-stock"


async def fetch_company(url):
    global data
    data = await fetch(url)


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_company(url))

company = Company.from_blob(data)
# print(company.price)
# print(company.code)
print(company.pne_ratio)
