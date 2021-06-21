import asyncio
import json

from pathlib import Path

from company_stocks.company import Company
from company_stocks.company_repository import CompanyRepository
from company_stocks.report import make_report


async def write_reports():
    """Write reports to files."""
    await Company.update_dollar_rate()

    all_companies = []
    repo = CompanyRepository()
    async for company in repo.get_all_companies():
        all_companies.append(company)

    path = Path(__file__).parent

    with open(path / "top_10_prices.json", "w") as fo:
        json.dump(make_report(all_companies, "price_in_rubles", reverse=True), fo)

    with open(path / "top_10_pne_ratio.json", "w") as fo:
        json.dump(make_report(all_companies, "pne_ratio"), fo)

    with open(path / "top_10_growth.json", "w") as fo:
        json.dump(make_report(all_companies, "growth", reverse=True), fo)

    with open(path / "top_10_profit.json", "w") as fo:
        json.dump(make_report(all_companies, "potential_profit", reverse=True), fo)


if __name__ == "__main__":
    asyncio.run(write_reports())
    print("finish")
