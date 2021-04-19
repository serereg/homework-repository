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
    """Return function with cashing results
    """
    memory = {}

    def func_with_memory(*x):
        if x not in memory:
            memory[x] = func(*x)
        return memory[x]

    return func_with_memory


if __name__ == "__main__":
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2

    # val_1 = cache_func(*some)
    # val_for_changing_cache = 123456
    # di = cache.memory
    # di[some] = val_for_changing_cache
    # val_for_changing_cache = cache_func(*some)
    
    # assert val_1 is val_for_changing_cache
