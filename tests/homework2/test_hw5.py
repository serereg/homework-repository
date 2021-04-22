import string

from homework2.hw5 import custom_range


def test_end_position_of_sequence():
    """Testing with choosing just and end position of given sequence
    custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
    """
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']


def test_begin_end_of_sequence():
    """Testing with choosing begin and end position of given sequence
    custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    """
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_full_args_of_sequence():
    """Testing choosing begin, end, step with given sequence
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
    """
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
