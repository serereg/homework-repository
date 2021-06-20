import asyncio
import json
import math
from operator import attrgetter

from company_stocks.company import Company
from company_stocks.company_repository import CompanyRepository


# TODO: use SQL
def make_report(companies: list, attr: str, num=10, reverse=False) -> list:
    """Form top num company by given arrtibute of Company class.

    Args:
        companies: list of companies.
        attr: an attribute of company by which companies should be
            sorted.
        num: number of companies to be returned.
        reverse: parameter of sort function.

    Return:
        list with dictionaries in format:
            [
                {
                    "code": "MMM",
                    "name": "3M CO.",
                    "price" | "P/E" | "growth" | "potential profit"
                        : value,
                },
                ...
            ]
    """
    li_ = [comp for comp in companies if not math.isnan(getattr(comp, attr))]
    li_.sort(key=attrgetter(attr), reverse=reverse)

    return [{"code": c.code, "name": c.name, attr: getattr(c, attr)} for c in li_[:num]]


async def write_reports():
    """Write reports to files."""
    await Company.update_dollar_rate()

    li = []
    repo = CompanyRepository()
    async for company in repo.get_all_companies():
        li.append(company)

    with open("top_10_prices.json", "w") as fo:
        json.dump(make_report(li, "price_in_rubles", reverse=True), fo)

    with open("top_10_pne_ratio.json", "w") as fo:
        json.dump(make_report(li, "pne_ratio"), fo)

    with open("top_10_growth.json", "w") as fo:
        json.dump(make_report(li, "growth", reverse=True), fo)

    with open("top_10_profit.json", "w") as fo:
        json.dump(make_report(li, "potential_profit", reverse=True), fo)


if __name__ == "__main__":
    asyncio.run(write_reports())
    print("finish")
