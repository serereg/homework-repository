from homeworks.homework1.task04 import check_sum_of_four


def test_sum_of_two():
    """Testing given sequences"""
    assert 2 == check_sum_of_four([1, 2], [-1, 0], [0, 0], [0, 10])


def test_sum_of_empy():
    """Testin empty sequences"""
    assert 0 == check_sum_of_four([], [], [], [])


def test_max_size():
    """Testing sequences with max amount of elements"""
    a = [0] * 1000
    b = [-1] * 1000
    c = [1] * 1000
    d = [0] * 1000
    assert 1000000000000 == check_sum_of_four(a, b, c, d)
