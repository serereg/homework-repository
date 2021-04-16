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

    result = current_sum = nums[0]
    box_of_k_elements = 0
    for ind in range(len(nums)):
        if box_of_k_elements == 0:
            result = current_sum = nums[0]
        elif box_of_k_elements < k:
            current_sum += nums[ind]
        else:
            current_sum += nums[ind]
            current_sum -= nums[ind - k]
        box_of_k_elements += 1
        # print(f'{ind=}, {current_sum=}')
        if current_sum > result:
            result = current_sum
    return result


if __name__ == "__main__":
    find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    find_maximal_subarray_sum([1, 2, 1, 6, 1, 1], 3)
