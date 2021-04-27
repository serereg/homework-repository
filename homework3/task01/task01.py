"""
In previous homework task 4, you wrote a cache function that remembers
other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use
 aw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""
from collections import namedtuple
from typing import Callable, Dict, Tuple


def cache_queue(times: int = 2):
    """Return function with cashing results.
    Caches 'times' results of calls
    """

    def cache(func: Callable) -> Callable:
        memory: Dict[Tuple, Callable] = {}
        FC = namedtuple("FC", ["fun_result", "calls_counter"])

        def func_with_memory(*args, **kwargs):
            arguments = args, tuple(sorted(kwargs.items()))
            if arguments in memory:
                fun_result, calls_counter = memory[arguments]
                calls_counter -= 1
                if calls_counter <= 0:
                    del memory[arguments]
                    print(f"cache with arguments {arguments} cleared")
                else:
                    memory[arguments] = FC(fun_result, calls_counter)
            if arguments not in memory:
                memory[arguments] = FC(func(*args, **kwargs), times)
                print(f"cache updated with {arguments}")
            return memory[arguments].fun_result

        return func_with_memory

    return cache


# def cache_queue(times: int = 2):
#     """Return function with cashing results"""
#
#     def cache(func: Callable) -> Callable:
#         memory: Dict[Tuple, List] = {}
#
#         def func_with_memory(*args, **kwargs):
#             full_arguments = args, tuple(sorted(kwargs.items()))
#             if full_arguments in memory:
#                 memory[full_arguments][1] -= 1
#                 if memory[full_arguments][1] <= 0:
#                     del memory[full_arguments]
#                     print(f"cache with arguments {full_arguments}
# cleared")
#             if full_arguments not in memory:
#                 memory[full_arguments] = [func(*args, **kwargs),
# times]
#                 print(f"cache updated with {full_arguments}")
#             return memory[full_arguments][0]
#
#         return func_with_memory
#
#     return cache


if __name__ == "__main__":

    @cache_queue(times=2)
    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    some = 10, 2

    val_1 = func(*some, c=2, d=3)
    print(f"{val_1=}")
    val_1 = func(*some, c=4, d=5)
    print(f"{val_1=}")
    val_1 = func(*some, c=4, d=5)
    print(f"{val_1=}")
    val_1 = func(*some, c=4, d=5)
    print(f"{val_1=}")
