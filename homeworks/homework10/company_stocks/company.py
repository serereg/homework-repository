import asyncio
import math

from .rate import Rate


class Company:
    """Class with business data of a company.

    Arguments:
        name: company name.
        code: code in a stock
        price: price in USD
        pne_ratio: price-earnings ratio
        growth: growth per year
        week52low: 52 Week Low
        week52high: 52 Week High
    """

    _dollar_rate = None

    def __init__(
        self,
        name: str,
        url: str,
        code="",
        price=0,
        pne_ratio=0,
        growth=0,
        week52low=0,
        week52high=0,
    ):
        self.name = name
        self.code = code
        self.price = price
        self.pne_ratio = pne_ratio
        self.growth = growth
        self._url = url
        self.week52low = week52low
        self.week52high = week52high

    def __str__(self):
        return f"{self.__dict__}"

    @classmethod
    def from_blob(cls, data: dict):
        """Create a company and fill attributes from a dictionary"""
        company = Company(data.get("Name", ""), data.get("URL", ""))
        company.price = float(data.get("Price", math.nan))
        company.code = data.get("Code", math.nan)
        company.pne_ratio = float(data.get("P/E Ratio", math.nan))
        company.growth = float(data.get("Growth", math.nan))
        company.week52low = float(data.get("52 Week Low", math.nan))
        company.week52high = float(data.get("52 Week High", math.nan))
        return company

    @property
    def url(self):
        """str: url of page company"""
        return self._url

    @property
    def profit(self):
        """float: difference between price at 52 week high and low"""
        return self.week52high - self.week52low

    @property
    def price_in_rubles(self):
        return self.price * Company._dollar_rate

    @classmethod
    async def update_dollar_rate(cls):
        cls._dollar_rate = await Rate().rate
        await asyncio.sleep(0)
