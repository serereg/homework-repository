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


def check_fibonacci(potential_fib: Sequence[int]) -> bool:
    """Check if the given sequence of int is a Febonacci sequence"""
    result = False
    if potential_fib is None or len(potential_fib) < 3:
        return False
    elif potential_fib == [0, 1, 1] and len(potential_fib) == 3:
        return True

    a, b, c = potential_fib[:3]

    while potential_fib:
        if not _check_window(a, b, c):
            result = False
            break
        if len(potential_fib) > 3:
            potential_fib = potential_fib[1:]
            a, b, c = b, c, potential_fib[2]
        else:
            result = True
            break
    return result
