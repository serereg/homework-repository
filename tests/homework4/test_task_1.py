import os
import pytest

from homework4.task_1_read_file import read_magic_number


directory = os.path.dirname(__file__)


def write_number_to_file(num_in_str: str, path: str):
    with open(path, "w") as fo:
        fo.write(num_in_str)


def test_read_number_from_interval():
    file_name = "data_for_test_1.txt"
    path = f"{directory}/{file_name}"
    write_number_to_file("1.1", path)
    assert read_magic_number(path) is True
    # TODO: remove file


def test_read_from_nonexisting_file():
    path = f"{directory}/nonexisting_file.txt"
    with pytest.raises(ValueError, match=r"in opening"):
        read_magic_number(path)


def test_read_not_a_number():
    file_name = "data_for_test_1.txt"
    path = f"{directory}/{file_name}"
    write_number_to_file("1asd1", path)
    with pytest.raises(ValueError, match=r"converting"):
        read_magic_number(path)


def test_read_an_empty_file():
    file_name = "data_for_test_1.txt"
    path = f"{directory}/{file_name}"
    write_number_to_file("", path)
    with pytest.raises(ValueError, match=r"converting"):
        read_magic_number(path)
