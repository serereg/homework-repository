"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Reads input line-by-line, and find maximum and minimum values.
    Function should return a tuple with the max and min values.

    Args:
        file_name (str): [description]

    Returns:
        Tuple[int, int]: [description]
    """    
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
