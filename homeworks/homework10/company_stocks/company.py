import math


class Company:
    """Class with business data of a company

    Arguments:
        name:
        profit:
        loss:
    """

    def __init__(self, name: str, url: str):
        self.name = name
        self.profit = 0
        self.loss = 0
        self.price = 0
        self._url = url
        self._blob = ""
        self.code = ""
        self.pne_ratio = 0
        self.growth = 0
        self.week52high = 0
        self.week52low = 0

    def __str__(self):
        return f"{self.pne_ratio, self.week52low, self.week52high}"

    @classmethod
    def from_blob(cls, data: dict):
        company = Company("", "")
        company.price = data.get("Price", math.nan)
        company.code = data.get("Code", math.nan)
        company.pne_ratio = data.get("P/E Ratio", math.nan)
        company.week52low = data.get("52 Week Low", math.nan)
        company.week52high = data.get("52 Week High", math.nan)
        return company

    @property
    def url(self):
        return self._url
