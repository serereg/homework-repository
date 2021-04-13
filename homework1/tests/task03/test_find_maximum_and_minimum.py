import pytest
from typing import Sequence
from task03 import find_maximum_and_minimum


def _write_sequence_to_file(some_file: str, sequence: Sequence[int]):
    with open(some_file, "w") as fi:
        for s in sequence:
            fi.write(f"{s}\n")
        fi.close

def test_file_with_one_value():
    """Testing file with one value"""
    some_file = "file_input.txt"
    sequence = (1,)
    _write_sequence_to_file(some_file, sequence)

    assert ((1, 1) == find_maximum_and_minimum(some_file))

def test_file_with_two_value():
    """Testing file with two values"""
    some_file = "file_input.txt"
    sequence = (2, 1)
    _write_sequence_to_file(some_file, sequence)

    assert ((1, 2) == find_maximum_and_minimum(some_file))

def test_file_with_three_value():
    """Testing file with three values"""
    some_file = "file_input.txt"
    sequence = (2, 1, 3)
    _write_sequence_to_file(some_file, sequence)

    assert ((min(sequence), max(sequence)) == find_maximum_and_minimum(some_file))
