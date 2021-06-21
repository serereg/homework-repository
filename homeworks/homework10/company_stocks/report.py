import math
from operator import attrgetter


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
    all_companies = [comp for comp in companies if not math.isnan(getattr(comp, attr))]
    all_companies.sort(key=attrgetter(attr), reverse=reverse)

    return [
        {"code": c.code, "name": c.name, attr: getattr(c, attr)}
        for c in all_companies[:num]
    ]
