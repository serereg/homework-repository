import asyncio

# import pytest

# from unittest.mock import Mock
from pathlib import Path

from homeworks.homework10.company_stocks.company_repository import CompanyRepository
from homeworks.homework10.company_stocks.rate import Rate


async def smoke_company_repository():
    repo = CompanyRepository()
    async for company in repo.get_all_companies():
        print(company)


async def fetch_company(url: str) -> str:
    path = Path(__file__).parent / "data/MMM Stock _ 3M.html"
    return path.read_text()


async def fetch_company_list(url: str) -> str:
    path = Path(__file__).parent / "data/S&P 500 Stock.html"
    return path.read_text()


def test_company_repository(monkeypatch):
    monkeypatch.setattr(CompanyRepository, "_fetch_company", fetch_company)
    monkeypatch.setattr(CompanyRepository, "_fetch_company_list", fetch_company_list)
    asyncio.run(smoke_company_repository())
    print("finish")
    # assert False
    assert True


async def fetch_dollar_page(url: str) -> str:
    path = Path(__file__).parent / "data/XML_daily.asp"
    await asyncio.sleep(0)
    return path.read_text(encoding="cp1251")


def test_parsing_dollar_rate(monkeypatch):
    monkeypatch.setattr(Rate, "_fetch", fetch_dollar_page)
    dollar = asyncio.run(Rate().rate)
    assert 72.22 < dollar < 72.23


# def test_parse_list_of_companies():
#     path = (
#             Path(__file__).parent /
#             "data/S&P 500 Stock _ S&P 500 Comp"
#                                     "anies _ S&
#             P 500 Value _ Markets Insider.html"
#     )
#     pages_src = [path.read_text()]
#     companies = parse_list_of_companies(pages_src)
#     print(companies)
#     assert False


# def test_parse_company():
#     path = (
#             Path(__file__).parent
#             / "data/MMM Stock _ 3M Stock
#             Price Today _ Markets Insider.html"
#     )
#     blob = path.read_text()
#     company = Company.from_blob(blob)
#     print(company)
#     assert False
#
