"""
Write a function that merges integer
from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path

from typing import List, Union, Iterator


def read_value_from_file(path: Union[Path, str]) -> Iterator:
    """Generate int numbers from file line-by-line.

    Args:
        path: file with integer numbers, written line-by-line.

    Example of file content:
    10
    34
    -2
    1
    4
    """
    with open(path) as fi:
        for line in fi:
            if line.isspace():
                continue
            yield int(line)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merge integer from sorted files.

    Args:
        file_list: list with files with sorted integers,
            written line-by-line.
    """
    values = []
    get_value_from_file = [read_value_from_file(file) for file in file_list]
    for file_num, file in enumerate(file_list):
        try:
            values.append(next(get_value_from_file[file_num]))
        except StopIteration:
            values.append(float("+inf"))

    while True:
        min_position = 0
        min_value = values[0]
        for i in range(1, len(values)):
            if values[i] < min_value:
                min_value = values[i]
                min_position = i
        if min_value == float("+inf"):
            return
        yield min_value

        try:
            values[min_position] = next(get_value_from_file[min_position])
        except StopIteration:
            values[min_position] = float("+inf")
