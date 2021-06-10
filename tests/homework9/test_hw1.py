from pathlib import Path

import pytest

from homeworks.homework9.hw1 import merge_sorted_files


@pytest.fixture()
def file_path(tmp_path: Path):
    def file_factory(body: str, file_name: str):
        """Creates a file with the given body text"""
        path = tmp_path.joinpath(file_name)
        path.write_text(body)
        return path

    return file_factory


def test_smoke(file_path):
    file_content = """0
    3
    5
    7
    10"""
    file1 = file_path(file_content, "file1.txt")
    file_content = """1
    2
    4
    6
    22"""
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [0, 1, 2, 3, 4, 5, 6, 7, 10, 22] == li


def test_with_different_length(file_path):
    file_content = """0
    3"""
    file1 = file_path(file_content, "file1.txt")
    file_content = """1
    2
    4
    6
    22"""
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [0, 1, 2, 3, 4, 6, 22] == li


def test_with_negative_integers(file_path):
    file_content = """0
    3"""
    file1 = file_path(file_content, "file1.txt")
    file_content = """-22
    -4
    1
    2
    6"""
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [-22, -4, 0, 1, 2, 3, 6] == li


def test_empty_files(file_path):
    file_content = """0
    3
    """
    file1 = file_path(file_content, "file1.txt")
    file_content = ""
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [0, 3] == li

    file_content = ""
    file1 = file_path(file_content, "file1.txt")
    file_content = ""
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [] == li


def test_with_duplicates_values(file_path):
    file_content = """0
    3
    """
    file1 = file_path(file_content, "file1.txt")
    file_content = """0
    3
    """
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [0, 0, 3, 3] == li


def test_files_with_spaces(file_path):
    file_content = """0


    3
    """
    file1 = file_path(file_content, "file1.txt")
    file_content = """-22
    -4
    1

    2

    6
    """
    file2 = file_path(file_content, "file2.txt")

    li = list(merge_sorted_files([file1, file2]))
    assert [-22, -4, 0, 1, 2, 3, 6] == li


def test_with_three_files(file_path):
    file_content = """0
    3
    """
    file1 = file_path(file_content, "file1.txt")
    file_content = """0
    3
    """
    file2 = file_path(file_content, "file2.txt")
    file_content = """1
    3
    """
    file3 = file_path(file_content, "file3.txt")

    li = list(merge_sorted_files([file1, file2, file3]))
    assert [0, 0, 1, 3, 3, 3] == li
