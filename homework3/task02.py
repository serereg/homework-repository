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


def sum_calcs(start: int = 0, stop: int = 501, num_processes: int = 10) -> int:
    """Calculating sum of num_calls calls slow_calculation
    function on num_process process
    """
    with multiprocessing.Pool(num_processes) as p:
        return sum(p.map(slow_calculate, range(start, stop)))


# TODO: how to process such operations?
def timer(func):
    """Measurement of function execution time"""

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return wrapper


def test_of_performance():
    """
    Prints correlation between number processes and time execution
    For intel core i7, u3630qm, 4x2400 MHz:
    [(1, 14.047987461090088), (6, 5.017956972122192),
    (11, 3.0253055095672607), (16, 3.0294504165649414),
    (21, 3.0380492210388184), (26, 3.04001522064209),
    (31, 3.040684938430786), (36, 3.0468456745147705),
    (41, 3.0469465255737305), (46, 3.059687852859497),
    (51, 3.062062978744507), (56, 3.070227861404419),
    (61, 3.0641942024230957), (66, 3.080547571182251),
    (71, 3.087139844894409), (76, 3.099928617477417),
    (81, 3.101140022277832), (86, 3.1148550510406494),
    (91, 3.112739324569702), (96, 3.1228690147399902)]
    """
    ti = timer(sum_calcs)
    times = map(
        lambda num_processes: (
            num_processes,
            ti(start=1, stop=10, num_processes=num_processes),
        ),
        range(1, 100, 5),
    )
    return times


if __name__ == "__main__":
    print(list(test_of_performance()))
