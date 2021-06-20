import asyncio
import json
import math

from company_stocks.company_repository import CompanyRepository
from company_stocks.company import Company

# from company_stocks.company import Company
from operator import attrgetter


# TODO: use SQL
def form_top_by_attr(companies: list, attr: str, num=10, reverse=False):
    li_ = [comp for comp in companies if not math.isnan(getattr(comp, attr))]
    li_.sort(key=attrgetter(attr), reverse=reverse)

    return [{"code": c.code, "name": c.name, attr: getattr(c, attr)} for c in li_[:num]]


async def write_reports():
    await Company.update_dollar_rate()

    li = []
    repo = CompanyRepository()
    async for company in repo.get_all_companies():
        li.append(company)

    with open("top_10_prices.json", "w") as fo:
        json.dump(form_top_by_attr(li, "price_in_rubles", reverse=True), fo)

    with open("top_10_pne_ratio.json", "w") as fo:
        json.dump(form_top_by_attr(li, "pne_ratio"), fo)

    with open("top_10_growth.json", "w") as fo:
        json.dump(form_top_by_attr(li, "growth", reverse=True), fo)

    with open("top_10_profit.json", "w") as fo:
        json.dump(form_top_by_attr(li, "profit", reverse=True), fo)


if __name__ == "__main__":
    asyncio.run(write_reports())
    print("finish")
