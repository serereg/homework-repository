"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest
from typing import Generator


def get_char_in_reserved_string(string: str) -> Generator[str, None, None]:
    """Generate sequence of chars from the given string.

    Sequence of chars return in a backward order.
    The '#' symbol means 'backspace'.

    Example:
        'asdfff##gh' -> 'h', 'g', 'f', 'd', 's', 'a'.

    Args:
        string: string, from which generates sequence
            of symbols.

    Returns:
        str: symbol from string without 'backspaces'.

    """
    string_reversed = reversed(string)
    counter_deletes = 0
    for s in string_reversed:
        if s == "#":
            counter_deletes += 1
            continue
        if counter_deletes > 0:
            counter_deletes -= 1
            continue
        yield s


def backspace_compare(first: str, second: str) -> bool:
    """Compare two strings, with # as backspace symbol.

    Args:
        first: string for a comparison.
        second: string for a comparison.

    Returns:
        bool: True, if strings are equal, False otherwise.

    Examples:
        if first is "ab#c" and second is "ad#c", then
        output is True.
        Both first and second become "ac".

        If first is "a##c" and second is "#a#c", then
        output is True.
        Both become "c".

        If first is "a#c" and second is "b", then
        output is False.
        First becomes "c" while second becomes "b".
    """
    first_and_second = zip_longest(
        get_char_in_reserved_string(first), get_char_in_reserved_string(second)
    )
    for f, s in first_and_second:
        if f != s:
            return False
    return True
