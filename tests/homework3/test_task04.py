from homework3.task04 import is_armstrong


def test_on_armstrong():
    list_of_armstrong_numbers = [0, 153]
    assert all(map(is_armstrong, list_of_armstrong_numbers)) is True


def test_with_non_armstrong():
    list_of_non_armstrong_numbers = [-1, 10, 20]
    assert any(map(is_armstrong, list_of_non_armstrong_numbers)) is False
