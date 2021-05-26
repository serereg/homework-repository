import hashlib
import struct

from homeworks.homework3.task02 import sum_calcs


def fast_clone_of_slow_calculate(value):
    """Some weird voodoo magic calculations"""
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def test_if_calls_sum_calcs_returns_right_result():
    summ = 0
    for i in range(501):
        summ += fast_clone_of_slow_calculate(i)
    assert sum_calcs() == summ
