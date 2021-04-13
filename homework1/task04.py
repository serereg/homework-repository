"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0

    # to exclude equal numbers
    short_a, short_b, short_c, short_d = set(a), set(b), set(c), set(d)

    for element in itertools.product(short_a, short_b, short_c, short_d):
        if not sum(element):
            result += 1

    return result
