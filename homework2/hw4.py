"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """Return function with cashing results"""
    memory = {}

    def func_with_memory(*args, **kwargs):
        full_arguments = (args, tuple(sorted(kwargs.items())))
        if (full_arguments) not in memory:
            memory[full_arguments] = func(*args, **kwargs)
        return memory[full_arguments]

    return func_with_memory


if __name__ == "__main__":

    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    cache_func = cache(func)
    some = 100, 200

    val_1 = cache_func(*some, c=2, d=3)
    val_2 = cache_func(*some, d=3, c=2)

    assert val_1 is val_2
