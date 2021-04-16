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
    if potential_fib is None or len(potential_fib) < 3:
        return False

    ind = 2
    while ind < len(potential_fib):
        j, k = ind - 2, ind + 1
        a, b, c = potential_fib[j:k]
        if not _check_window(a, b, c):
            return False
        ind += 1
    return True


if __name__ == "__main__":
    check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13])
