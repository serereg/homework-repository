import pytest
from pathlib import Path

from homeworks.homework4.task_1_read_file import read_magic_number


@pytest.fixture()
def file_path(tmp_path: Path):
    def file_factory(body: str, file_name: str):
        """Creates a file with the given body text"""
        path = tmp_path.joinpath(file_name)
        path.write_text(body)
        return path

    return file_factory


def test_read_number_from_interval(file_path):
    path = file_path("1.1", "data_for_task_1.txt")
    assert read_magic_number(path) is True


def test_read_number_from_borders(file_path):
    path = file_path("1.00", "data_for_task_1.txt")
    assert read_magic_number(path) is True
    path = file_path("2.99", "data_for_task_1.txt")
    assert read_magic_number(path) is True


def test_read_number_out_from_interval(file_path):
    path = file_path("-100", "data_for_task_1.txt")
    assert read_magic_number(path) is False


def test_read_not_a_number(file_path):
    path = file_path("1asd1", "data_for_task_1.txt")
    with pytest.raises(ValueError, match=r"converting"):
        read_magic_number(path)


def test_read_an_empty_file(file_path):
    path = file_path("", "data_for_task_1.txt")
    with pytest.raises(ValueError, match=r"converting"):
        read_magic_number(path)


def test_read_from_nonexisting_file():
    path = f"{Path(__name__).parent}/nonexisting_file.txt"
    with pytest.raises(ValueError, match=r"not found"):
        read_magic_number(path)
