import asyncio
from decimal import Decimal
from re import sub

import aiohttp
from bs4 import BeautifulSoup


class Rate:
    """A class for operating with currencies."""

    def __init__(
        self, url="http://www.cbr.ru/scripts/XML_daily.asp", valute_id="R01235"
    ):
        self._url = url
        self._valute_id = valute_id
        self._rate = None

    @staticmethod
    async def _fetch(url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise ValueError(f"Can't open url: {url}")
                return await resp.text()

    @staticmethod
    def _parse_currency_page(valute: str, page: str):
        soup = BeautifulSoup(page, "lxml")
        return float(
            Decimal(sub(r"[^\d.]", ".", soup.find(id=valute).find("value").text))
        )

    @property
    async def rate(self) -> float:
        """Get current currency"""
        if not self._rate:
            page = await Rate._fetch(self._url)
            self._rate = Rate._parse_currency_page(self._valute_id, page)
        return self._rate


async def main():
    dollar = await Rate().rate
    print(dollar)


if __name__ == "__main__":
    asyncio.run(main())
