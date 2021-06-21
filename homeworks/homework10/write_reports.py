import asyncio
import json

from pathlib import Path

from company_stocks.company import Company
from company_stocks.company_repository import CompanyRepository
from company_stocks.report import make_report


def write_reports():
    """Write reports to files."""
    asyncio.run(Company.update_dollar_rate())

    repo = CompanyRepository()

    path = Path(__file__).parent
    path_prices = path / "top_10_prices.json"
    path_pne = path / "top_10_pne_ratio.json"
    path_growth = path / "top_10_growth.json"
    path_profit = path / "top_10_profit.json"

    path_prices.write_text(
        json.dumps(
            make_report(repo.get_all_companies(), "price_in_rubles", reverse=True)
        )
    )
    path_pne.write_text(json.dumps(make_report(repo.get_all_companies(), "pne_ratio")))
    path_growth.write_text(
        json.dumps(make_report(repo.get_all_companies(), "growth", reverse=True))
    )
    path_profit.write_text(
        json.dumps(
            make_report(repo.get_all_companies(), "potential_profit", reverse=True)
        )
    )


if __name__ == "__main__":
    write_reports()
    print("finish")
