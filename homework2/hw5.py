"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:

import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
def custom_range(iter, *args):
    """function that accept any iterable of unique values and then
    it behaves as range function
    Args:
        iter ([type]): [description]
    """
    if len(args) == 1:
        start, stop, step = args[0], args[0], 1
    if len(args) == 2:
        start, stop, step = args[0], args[1], 1
    if len(args) == 3:
        start, stop, step = args

    print(start, stop, step)
    # iter.reverse()
    # for i, k in enumerate(iter):
        # print(i, k)
    # a = list(1, 2, 3, 4)
    a = iter.index(start)
    b = iter.index(stop)
    return iter[a:b:step]
    