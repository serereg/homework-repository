import asyncio

from company_stocks.company_repository import CompanyRepository


def make_report():
    for company in CompanyRepository("url").get_all_companies():
        net_profit = company.profit - company.loss
        print(f"Net profit for {company.name} is {net_profit}")


async def foo():
    repo = CompanyRepository()
    async for company in repo.get_all_companies():
        print(company)
    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(foo())
    print("finish")
