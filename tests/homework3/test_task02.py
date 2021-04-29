from homework3.task02 import slow_calculate, sum_calcs


def test_is_calls_sum_calcs_the_same_as_slow_calculate():
    sum: int = 0
    for i in range(3):
        sum += slow_calculate(i)

    assert sum_calcs(num_calls=3, num_process=1) == sum
