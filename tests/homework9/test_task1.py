from pathlib import Path

import pytest

from homeworks.homework9.hw1 import read_value_from_file


@pytest.fixture()
def file_path(tmp_path: Path):
    def file_factory(body: str, file_name: str):
        """Creates a file with the given body text"""
        path = tmp_path.joinpath(file_name)
        path.write_text(body)
        return path

    return file_factory


def test_access_to_attributes(file_path):
    file_content = """1
    3
    5
    7
    10"""
    file1 = file_path(file_content, "file1.txt")
    # file_content = """0
    # 2
    # 4
    # 6
    # 22"""
    # file2 = file_path(file_content, "file2.txt")

    values_from_file1 = read_value_from_file(file1)
    assert 1 == next(values_from_file1)
    assert 3 == next(values_from_file1)
    assert 5 == next(values_from_file1)
