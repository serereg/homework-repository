import math


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

    def __init__(
        self,
        name: str,
        url: str,
        code="",
        price="",
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
        return f"{self.pne_ratio, self.week52low, self.week52high}"

    @classmethod
    def from_blob(cls, data: dict):
        """Create a company and fill attributes from a dictionary"""
        company = Company(data.get("Name", ""), data.get("URL", ""))
        company.price = data.get("Price", math.nan)
        company.code = data.get("Code", math.nan)
        company.pne_ratio = data.get("P/E Ratio", math.nan)
        company.week52low = data.get("52 Week Low", math.nan)
        company.week52high = data.get("52 Week High", math.nan)
        return company

    @property
    def url(self):
        """str: url of page company"""
        return self._url

    @property
    def profit(self):
        """float: difference between price at 52 week high and low"""
        return self.week52high - self.week52low
