"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of
    integers, and returns if the given sequence is
    a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    """Check if x, y, z is a Fibonacci sequence"""
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check if the given sequence of int is a Febonacci sequence"""
    result = False
    if data in (None, [0], [0, 1]):
        result = False
    elif data == [0, 1, 1]:
        result = True
    elif len(data) > 3:
        a, b, c = data[0], data[1], data[2]

        while data:
            print(a, b, c)
            if not _check_window(a, b, c):
                result = False
                break
            if len(data) > 3:
                data = data[1:]
                a, b, c = b, c, data[2]
            else:
                result = True
                break
    return result
