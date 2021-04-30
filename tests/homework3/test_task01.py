from homework3.task01 import cache_queue


def testing_smoke():
    """Testing usual behaviour"""

    @cache_queue(times=2)
    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    some = 10, 2

    assert 10005 == func(*some, c=2, d=3)
    assert 10009 == func(*some, c=4, d=5)
    assert 10009 == func(*some, c=4, d=5)
    assert 10009 == func(*some, c=4, d=5)
    # TODO: some enhancements should be done accordint to lecture04
