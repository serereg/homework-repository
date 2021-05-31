from homeworks.homework2.hw4 import cache


def test_smoke():
    """
    Testing usual behavior
    """

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_with_kwargs():
    """
    Testing usual behavior with kwargs
    """

    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    cache_func = cache(func)
    some = 100, 200

    val_1 = cache_func(*some, c=2, d=3)
    val_2 = cache_func(*some, d=3, c=2)

    assert val_1 is val_2

    val_1 = cache_func(*some, c=0, d=3)
    val_2 = cache_func(*some, d=3, c=2)

    assert val_1 is not val_2
