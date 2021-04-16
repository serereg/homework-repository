"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k",
    with maximal sum.
The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Given a list of integers numbers "nums".
    You need to find a sub-array with length less equal to "k",
        with maximal sum.
    The written function should return the sum of this sub-array.

    Examples:
        nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        result = 16
    """
    if k <= 0 or len(nums) == 0:
        raise ValueError("Not a list given to the function.")

    result = 0
    subarr = [0] * k
    for num in nums:
        subarr.pop(0)
        subarr.append(num)
        current_sum = sum(subarr)
        if current_sum > result:
            result = current_sum

    return result
