"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:

import string


assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iter, *args):
    """function that accept any iterable of unique values and then
    it behaves as range function

    Args:
        iter (iterable, start_elemeng):
        iter (iterable, start_elemeng, stop_element):
        iter (iterable, start_elemeng, stop_element, step):

    Example:
    assert = custom_range(string.ascii_lowercase, 'g') ==
                        ['a', 'b', 'c', 'd', 'e', 'f']
    assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
                        ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
                        ['p', 'n', 'l', 'j', 'h']
    """
    if len(args) == 1:
        start_element, stop_element, step = None, args[0], None
    if len(args) == 2:
        start_element, stop_element, step = args[0], args[1], None
    if len(args) == 3:
        start_element, stop_element, step = args
    begin = 0
    if start_element:
        begin = iter.index(start_element)
    end = iter.index(stop_element)
    return [element for element in iter[begin:end:step]]
