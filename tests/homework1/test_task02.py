from homework1.task02 import check_fibonacci


def test_empty_sequence():
    """Testing empty sequence"""
    assert check_fibonacci([]) is False


def test_first_3_sequence():
    """ """
    assert check_fibonacci([0]) is False
    assert check_fibonacci([0, 1]) is False
    assert check_fibonacci([0, 1, 1]) is True


def test_normal():
    """Testing that zero give False"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8]) is True


# TODO: write test for 65536 (or biggest integer)

# TODO: write test for [1, 1, 2, ...]


def test_last_number_of_sequence():
    """Testing all numbers are cheked """
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 7]) is False
