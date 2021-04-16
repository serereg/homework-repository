from typing import Sequence

from homework1.task03 import find_maximum_and_minimum


def _write_sequence_to_file(some_file: str, sequence: Sequence[int]):
    """Writing sequence to the file

    Args:
        some_file (str): [description]
        sequence (Sequence[int]): [description]
    """

    with open(some_file, "w") as fo:
        for s in sequence:
            fo.write(f"{s}\n")
        fo.close


def _read_sequence_from_file(some_file: str) -> Sequence[int]:
    """Reading sequence from the file

    Args:
        some_file (str): [description]

    Returns:
        Sequence[int]: [description]
    """
    sequence = []
    with open(some_file) as fi:
        for num in fi.readlines():
            sequence.append(int(num))
        fi.close
    return sequence


def test_file_with_one_value():
    """Testing file with one value"""
    some_file = "tests/homework1/test_data/task03_case1.txt"
    sequence = _read_sequence_from_file(some_file)
    assert (min(sequence), max(sequence)) == find_maximum_and_minimum(some_file)


def test_file_with_two_value():
    """Testing file with two values"""
    some_file = "tests/homework1/test_data/task03_case2.txt"
    sequence = _read_sequence_from_file(some_file)
    assert (min(sequence), max(sequence)) == find_maximum_and_minimum(some_file)


def test_file_with_three_value():
    """Testing file with three values"""
    some_file = "tests/homework1/test_data/task03_case3.txt"
    sequence = _read_sequence_from_file(some_file)
    assert (min(sequence), max(sequence)) == find_maximum_and_minimum(some_file)
