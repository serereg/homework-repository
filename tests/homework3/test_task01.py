from unittest.mock import Mock, call

from homeworks.homework3.task01 import cache_queue


def test_smoke():
    """Testing usual behaviour"""

    @cache_queue(times=2)
    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    some = 10, 2

    assert 10005 == func(*some, c=2, d=3)
    assert 10009 == func(*some, c=4, d=5)
    assert 10009 == func(*some, c=4, d=5)
    assert 10009 == func(*some, c=4, d=5)
    # TODO: some enhancements should be done according to lecture04


def test_cached():
    mock = Mock()
    cached_function = cache_queue(times=2)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3), call(1, 3)]
