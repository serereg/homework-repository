import pytest

from homeworks.homework1.task05 import find_maximal_subarray_sum


def test_smoke():
    """Test of task sequense"""
    assert 16 == find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3)


def test_empty_arr():
    """Test of empty sequence"""
    with pytest.raises(ValueError):
        find_maximal_subarray_sum([], 3)


def test_empty_subarr():
    """Test of zero subarray"""
    with pytest.raises(ValueError):
        find_maximal_subarray_sum([1, 3, 1, 4], 0)


def test_of_negative_array():
    """Test of task sequense"""
    assert -4 == find_maximal_subarray_sum([-20, -1, -2, -1, -30, -10, -10], 3)


def test_of_positive_array():
    """Test of task sequense"""
    assert 9 == find_maximal_subarray_sum([1, 2, 1, 6, 1, 1], 3)
