"""
Write a function that takes K lists as arguments and
returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least
one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    """
    Returns all combinations of given lists in a list
    """
    return [list(item) for item in itertools.product(*args)]


if __name__ == "__main__":
    all_combinations = combinations([1, 2], [4, 3])
    for i in all_combinations:
        print(i, type(i))
    print(all_combinations)
