from homeworks.homework2.hw3 import combinations


def test_smoke():
    all_combinations = combinations([1, 2], [4, 3])
    assert all_combinations == [[1, 4], [1, 3], [2, 4], [2, 3]]
