def check_power_of_2(a: int) -> bool:
    result = False
    if a > 0:
        result = not (bool(a & (a - 1)))

    return result
