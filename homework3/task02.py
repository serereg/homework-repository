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


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_calcs(num_calls: int = 1, num_process: int = 1) -> int:
    """Calculating sum of num_calls calls slow_calculation
    function on num_process process
    """
    with multiprocessing.Pool(num_process) as p:
        return sum(p.map(slow_calculate, [i for i in range(num_calls)]))
