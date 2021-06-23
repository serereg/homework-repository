import asyncio
import json

# import pytest

# from unittest.mock import Mock
from pathlib import Path
from typing import List

from homeworks.homework10.company_stocks.company import Company
from homeworks.homework10.company_stocks.company_repository import CompanyRepository
from homeworks.homework10.company_stocks.rate import Rate
from homeworks.homework10.company_stocks.report import make_report


def parse_company_repository():
    repo = CompanyRepository()
    li = []
    for company in repo.get_all_companies():
        li.append(company)
    assert len(li) == 2

    assert li[0].code == "MMM"
    assert li[0].growth == 31.19
    assert li[0].pne_ratio == 19.91
    assert round(li[0].potential_profit) == 60

    assert li[1].growth == 44.93
    return True


async def fetch_companies(*args) -> List:
    path1 = Path(__file__).parent / "data/MMM Stock _ 3M.html"
    path2 = Path(__file__).parent / "data/AOS Stock.html"
    await asyncio.sleep(0)
    return [path1.read_text(), path2.read_text()]


async def fetch_tables_with_companies(*args) -> List[str]:
    path = Path(__file__).parent / "data/S&P 500 Stock.html"
    await asyncio.sleep(0)
    return [path.read_text()]


def test_company_repository(monkeypatch):
    monkeypatch.setattr(CompanyRepository, "_get_all_detailed_pages", fetch_companies)
    monkeypatch.setattr(
        CompanyRepository, "_get_all_table_pages", fetch_tables_with_companies
    )
    assert parse_company_repository() is True


async def fetch_dollar_page(url: str) -> str:
    path = Path(__file__).parent / "data/XML_daily.asp"
    await asyncio.sleep(0)
    return path.read_text(encoding="cp1251")


def test_parsing_dollar_rate(monkeypatch):
    monkeypatch.setattr(Rate, "_fetch", fetch_dollar_page)
    dollar = asyncio.run(Rate().rate)
    assert 72.22 < dollar < 72.23


async def form_reports():
    await Company.update_dollar_rate()

    company1 = Company("c1", "")
    company1.code = "c1"
    company1.price = 1
    company1.pne_ratio = 1
    company1.growth = 1
    company1.week52low = 0
    company1.week52high = 1

    company2 = Company("c2", "")
    company2.code = "c2"
    company2.price = 2
    company2.pne_ratio = 2
    company2.growth = 2
    company2.week52low = 0
    company2.week52high = 2

    all_companies = [company1, company2]

    return (
        json.dumps(make_report(all_companies, "price_in_rubles", reverse=True)),
        json.dumps(make_report(all_companies, "pne_ratio")),
        json.dumps(make_report(all_companies, "growth", reverse=True)),
        json.dumps(make_report(all_companies, "potential_profit", reverse=True)),
    )


def test_report(monkeypatch):
    monkeypatch.setattr(CompanyRepository, "_get_all_detailed_pages", fetch_companies)
    monkeypatch.setattr(
        CompanyRepository, "_get_all_table_pages", fetch_tables_with_companies
    )
    monkeypatch.setattr(Rate, "_fetch", fetch_dollar_page)
    result = asyncio.run(form_reports())
    assert result == (
        json.dumps(
            [
                {"code": "c2", "name": "c2", "price_in_rubles": 144.4432},
                {"code": "c1", "name": "c1", "price_in_rubles": 72.2216},
            ]
        ),
        json.dumps(
            [
                {"code": "c1", "name": "c1", "pne_ratio": 1},
                {"code": "c2", "name": "c2", "pne_ratio": 2},
            ]
        ),
        json.dumps(
            [
                {"code": "c2", "name": "c2", "growth": 2},
                {"code": "c1", "name": "c1", "growth": 1},
            ]
        ),
        json.dumps(
            [
                {"code": "c2", "name": "c2", "potential_profit": 2},
                {"code": "c1", "name": "c1", "potential_profit": 1},
            ]
        ),
    )
