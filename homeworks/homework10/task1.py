import aiohttp  # import: ignore
from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen(
    "https://stepik.org/media/attachments/lesson/245130/6.html"
)  # скачиваем файл
html = resp.read().decode("utf8")  # считываем содержимое
soup = BeautifulSoup(html, "html.parser")  # делаем суп
table = soup.find("table", attrs={"class": "wikitable sortable"})
cnt = 0
for tr in soup.find_all("tr"):
    cnt += 1
    for td in tr.find_all(["td", "th"]):
        cnt *= 2
print(cnt)


# import asyncio


class Company:
    def __init__(self):
        self.profit = 0
        self.loss = 0

    @classmethod
    async def from_blob(cls, data):
        pass


class CompanyRepository:
    def __init__(self, url):
        self._cache = []
        self._url = url

    @staticmethod
    def _parse_company_list(self, page):
        yield None

    async def get_all_companies(self):
        if self._cache:
            for item in self._cache:
                yield item
        else:
            # create a list of tasks to execute
            # get_data_page(page_number) for page_number in range(10)
            async with aiohttp.ClientSession() as session:
                async with session.get(self._url) as resp:
                    company_list_page = await resp.text()

        for company_blob in self._parse_company_list(company_list_page):
            company = await Company.from_blob(company_blob)
            yield company
            self._cache.append(company)


def make_report():
    for company in CompanyRepository("url").get_all_companies():
        net_profit = company.profit - company.loss
        print(f"Net profit for {company.name} is {net_profit}")
