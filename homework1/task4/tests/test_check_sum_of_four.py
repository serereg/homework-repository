import pytest
from check_sum_of_four.check_sum_of_four import check_sum_of_four

def test_sum_of_two():
    assert 3 == check_sum_of_four([-1, 0, 1], [-1, 0, 1], [0, 0, 0], [0, 0, 0])
    