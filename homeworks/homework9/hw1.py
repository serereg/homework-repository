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
    values = [float("+inf") for i in file_list]
    gens = [read_value_from_file(file) for file in file_list]
    while True:
        for file_num, file in enumerate(file_list):
            try:
                if values[file_num] == float("+inf"):
                    values[file_num] = next(gens[file_num])
            except StopIteration:
                values[file_num] = float("+inf")
        if all([i == float("+inf") for i in values]):
            return
        min_value = min(values)
        values[values.index(min_value)] = float("+inf")
        yield min_value
