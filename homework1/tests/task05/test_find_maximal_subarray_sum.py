import pytest
from task05 import \
    find_maximal_subarray_sum


def test_smoke():
    """Test of task sequense"""
    assert 16 == find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3)


def test_empty_arr():
    """Test of empty sequence"""
    assert None == find_maximal_subarray_sum([], 3)


def test_empty_subarr():
    """Test of zero subarray"""
    assert None == find_maximal_subarray_sum([1, 3, 1, 4], 0)
