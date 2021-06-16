from pathlib import Path

from homeworks.homework10.train1 import Company, parse_list_of_companies


def test_parse_list_of_companies():
    path = (
        Path(__file__).parent / "data/S&P 500 Stock _ S&P 500 Comp"
        "anies _ S&P 500 Value _ Markets Insider.html"
    )
    pages_src = [path.read_text()]
    companies = parse_list_of_companies(pages_src)
    print(companies)
    assert False


def test_parse_company():
    path = (
        Path(__file__).parent
        / "data/MMM Stock _ 3M Stock Price Today _ Markets Insider.html"
    )
    blob = path.read_text()
    company = Company.from_blob(blob)
    print(company)
    assert False
