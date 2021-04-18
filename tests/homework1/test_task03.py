import os
from typing import Sequence

from homework1.task03 import find_maximum_and_minimum


def test_file_with_one_value():
    """Testing file with one value"""
    some_file = os.path.dirname(__file__) + "/test_data/task03_case1.txt"
    sequence = []
    with open(some_file) as fi:
        for num in fi.readlines():
            sequence.append(int(num))
    assert (min(sequence), max(sequence)) == find_maximum_and_minimum(some_file)


def test_file_with_two_value():
    """Testing file with two values"""
    some_file = os.path.dirname(__file__) + "/test_data/task03_case2.txt"
    sequence = []
    with open(some_file) as fi:
        for num in fi.readlines():
            sequence.append(int(num))
    assert (min(sequence), max(sequence)) == find_maximum_and_minimum(some_file)


def test_file_with_three_value():
    """Testing file with three values"""
    some_file = os.path.dirname(__file__) + "/test_data/task03_case3.txt"
    sequence = []
    with open(some_file) as fi:
        for num in fi.readlines():
            sequence.append(int(num))
    assert (min(sequence), max(sequence)) == find_maximum_and_minimum(some_file)
