"""
    Classic task, a kind of walnut for you

    Given four lists A, B, C, D of integer values,
        compute how many tuples (i, j, k, l) there are such
        that A[i] + B[j] + C[k] + D[l] is zero.

    We guarantee, that all A, B, C, D have same length of N
        where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List
from typing import Dict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Given four lists A, B, C, D of integer values.
    Function computes how many tuples (i, j, k, l) there are such
        that A[i] + B[j] + C[k] + D[l] is zero.

    All A, B, C, D must have same length of N
        where 0 ≤ N ≤ 1000.

        https://medium.com/@hylei_73413/4-sum-cf5e47f36126
    """
    e: Dict[int, int] = {}
    for element in itertools.product(a, b):
        e[sum(element)] = e.get(sum(element), 0) + 1

    f: Dict[int, int] = {}
    for element in itertools.product(c, d):
        f[sum(element)] = f.get(sum(element), 0) + 1

    count: int = 0
    for e_key in e.keys():
        if f.get(-e_key):
            count += e.get(e_key, 0) * f.get(-e_key, 0)
    return count


if __name__ == "__main__":
    n = check_sum_of_four([1] * 2, [-1] * 2, [0] * 2, [0] * 2)
    print(n)
