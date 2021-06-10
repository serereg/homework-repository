import pytest

from pathlib import Path, PurePath

from homeworks.homework9.hw3 import universal_file_counter

path = Path(PurePath(__file__).parent).joinpath("test_data_task3")
empty_path = (
    Path(PurePath(__file__).parent).joinpath("test_data_task3").joinpath("empty_dir")
)


def test_count_lines():
    assert 12 == universal_file_counter(path, "txt")
    assert True


def test_another_tokenizer():
    def get_symbol(path: Path):
        with path.open() as fi:
            for line in fi:
                yield from line

    assert 166 + 132 == universal_file_counter(path, "txt", get_symbol)


def test_empty_path():
    assert 0 == universal_file_counter(empty_path, "txt")


def test_path_is_not_a_dir():
    with pytest.raises(IOError):
        universal_file_counter(Path("not a path"), "txt")
