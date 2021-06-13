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
import heapq
from pathlib import Path
from typing import Iterator, List, Tuple, Union


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
    values: List[Tuple[Union[float, int], int]] = []
    get_from_file = [read_value_from_file(file) for file in file_list]
    for file_num, file in enumerate(file_list):
        try:
            heapq.heappush(values, (next(get_from_file[file_num]), file_num))
        except StopIteration:
            heapq.heappush(values, (float("+inf"), file_num))

    while True:
        min_value, file_min_value = heapq.heappop(values)

        if min_value == float("+inf"):
            return

        try:
            heapq.heappush(
                values, (next(get_from_file[file_min_value]), file_min_value)
            )
        except StopIteration:
            heapq.heappush(values, (float("+inf"), file_min_value))

        yield min_value
