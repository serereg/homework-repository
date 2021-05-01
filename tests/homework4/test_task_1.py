import os
import pytest

from homework4.task_1_read_file import read_magic_number


directory = os.path.dirname(__file__)


def write_number_to_file(num: float, path: str):
    with open(path, "w") as fo:
        fo.write(str(num))


def test_read_number_from_interval():
    file_name = "data_for_test_1.txt"
    path = f"{directory}/{file_name}"
    write_number_to_file(1.1, path)
    assert read_magic_number(path) is True
    # TODO: remove file


def test_read_from_nonexisting_file():
    path = f"{directory}/nonexisting_file.txt"
    with pytest.raises(ValueError, match="Some exception"):
        read_magic_number(path)


# TODO: read an empty file
# read several numbers
# read not a number
