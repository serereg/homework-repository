import os

from homework2.hw1 import (
    get_longest_diverse_words,
    get_rarest_char,
    count_punctuation_chars,
    get_most_common_non_ascii_char,
    count_punctuation_chars_with_tokenize,
)


test_data_hw1 = os.path.dirname(__file__) + "/test_data/data_hw1.txt"
test_data_short = os.path.dirname(__file__) + "/test_data/data_short.txt"


def test_get_longest_diverse_words():
    """Testing function get_longest_divetse_words"""
    assert [
        "vorgebahnte",
        "ausführen",
        "bedenkli-",
        "vielmehr",
        "sondern",
        "grenzen",
        "wird",
        "der",
        "es",
        "—",
    ] == get_longest_diverse_words(test_data_hw1)


def test_get_rarest_char():
    """Testing getting rarest char from given text"""
    assert "1" == get_rarest_char(test_data_short)


def test_count_punctuation_chars():
    """Testing punctuation counter from given text"""
    assert 5 == count_punctuation_chars(test_data_short)


def test_get_most_common_non_ascii_char():
    """Testing getting the most common non ascit char from given text"""
    assert "\u00bb" == get_most_common_non_ascii_char(test_data_short)


def test_count_punctuation_chars_with_tokenize():
    """Testing counter of punctuation with tokenize"""
    assert 5 == count_punctuation_chars_with_tokenize(test_data_short)
