import heapq
import math

from typing import List, Tuple


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
    # all_companies = [comp for comp in
    # companies if not math.isnan(getattr(comp, attr))]
    # all_companies.sort(key=attrgetter(attr), reverse=reverse)

    all_companies: List[Tuple] = []
    sign = -1 if reverse is True else 1
    for comp in companies:
        value = getattr(comp, attr)
        if value is math.nan:
            continue
        heapq.heappush(all_companies, (value * sign, comp))

    size = min(num, len(all_companies))
    top = [heapq.heappop(all_companies)[1] for i in range(size)]
    return [
        {"code": c.code, "name": c.name, attr: getattr(c, attr)} for c in top[:size]
    ]
