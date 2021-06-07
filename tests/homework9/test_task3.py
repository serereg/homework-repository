from pathlib import Path, PurePath

from homeworks.homework9.hw3 import universal_file_counter


path = Path(PurePath(__file__).parent).joinpath("test_data_task3")


def test_count_lines():
    assert 12 == universal_file_counter(path, "txt")
    assert True
