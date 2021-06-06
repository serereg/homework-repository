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


def read_value_from_file(path: Union[Path, str]):
    with open(path) as fi:
        for line in fi:
            yield int(line)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    values = [float("+inf") for i in file_list]
    gens = [read_value_from_file(file) for file in file_list]
    while True:
        for file_num, file in enumerate(file_list):
            try:
                if values[file_num] == float("+inf"):
                    values[file_num] = next(gens[file_num])
            except StopIteration:
                values[file_num] = float("+inf")
        min_value = min(values)
        print(values, min_value)
        values[values.index(min_value)] = float("+inf")
        print(values)
        yield min_value
        if all([i == float("+inf") for i in values]):
            return
