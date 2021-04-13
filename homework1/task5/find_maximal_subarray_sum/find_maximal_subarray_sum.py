from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k <= 0 or len(nums) == 0:
        return None

    result = 0
    subarr = [0] * k
    for num in nums:
        subarr.pop(0)
        subarr.append(num)
        current_sum = sum(subarr)
        if current_sum > result:
            result = current_sum

    return result
