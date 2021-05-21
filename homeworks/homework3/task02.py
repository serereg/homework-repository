"""Here's a not very efficient calculation function
that calculates something important::

Calculate total sum of slow_calculate() of all numbers
starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

import hashlib
import multiprocessing
import random
import struct
import time
from typing import Dict


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_calcs(start: int = 0, stop: int = 501, num_processes: int = 10) -> int:
    """Calculating sum of num_calls calls slow_calculation
    function on num_process process
    """
    with multiprocessing.Pool(num_processes) as p:
        return sum(p.map(slow_calculate, range(start, stop)))


def timeit(log_time: Dict[str, int]):
    """
    Logs execution time of the method in log_time dictionary
    """

    def wrapper(method):
        def inner(*args, **kwargs):
            ts = time.time()
            result = method(*args, **kwargs)
            te = time.time()
            log_time[f"{method.__name__}, {args=}, {kwargs=}"] = int((te - ts) * 1000)
            return result

        return inner

    return wrapper


if __name__ == "__main__":
    logtime_data: Dict[str, int] = {}
    ti = timeit(log_time=logtime_data)(sum_calcs)
    for num_processes in range(1, 100, 5):
        ti(start=1, stop=10, num_processes=num_processes)

    for i in logtime_data.items():
        print(i)
