from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    min_value, max_value = None, None
    number_of_values = 0
    with open(file_name) as fi:
        for line in fi:
            current_value = int(line)
            number_of_values += 1
            if number_of_values == 1:
                min_value = current_value
                max_value = current_value
            else:
                if current_value < min_value:
                    min_value = current_value
                if current_value > max_value:
                    max_value = current_value

    return (min_value, max_value)

