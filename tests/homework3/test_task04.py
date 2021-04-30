from homework3.task04 import is_armstrong


def test_on_armstrong():
    assert is_armstrong(153) is True
    assert is_armstrong(0) is True


def test_with_non_armstrong():
    assert is_armstrong(10) is False
