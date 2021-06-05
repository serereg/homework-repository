from pathlib import Path

import pytest

from homeworks.homework8.task1 import ErrInDictFile, KeyValueStorage


@pytest.fixture()
def file_path(tmp_path: Path):
    def file_factory(body: str, file_name: str):
        """Creates a file with the given body text"""
        path = tmp_path.joinpath(file_name)
        path.write_text(body)
        return path

    return file_factory


def test_access_to_attributes(file_path):
    file_content = """name=kek
    last_name=top
    power=9001
    song=shadilay
    cnt=1"""
    dict_file = file_path(file_content, "tmp_file.txt")
    storage = KeyValueStorage(dict_file)
    assert hasattr(storage, "name") is True
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage["power"] == 9001
    assert storage["song"] == "shadilay"
    assert storage["cnt"] == 1
    assert storage.name == "kek"


def test_existing_key(file_path):
    file_content = """last_name=top
    __dir__=1
    first_name=sam"""
    dict_file = file_path(file_content, "tmp_file.txt")

    storage = KeyValueStorage(dict_file)
    assert storage["__dir__"] == 1
    assert isinstance(storage.__dir__(), list)


def test_access_to_non_exesting_attributes(file_path):
    file_content = """name=kek
    last_name=top
    cnt=1"""
    dict_file = file_path(file_content, "tmp_file.txt")
    storage = KeyValueStorage(dict_file)
    with pytest.raises(KeyError) as err:
        storage["wrong"] == 1
    assert "key" in str(err.value)


def test_err_key(file_path):
    file_content = """1=kek
    last_name=top
    cnt=1"""
    dict_file = file_path(file_content, "tmp_file.txt")
    with pytest.raises(ValueError):
        KeyValueStorage(dict_file)


def test_empty_file(file_path):
    file_content = ""
    dict_file = file_path(file_content, "tmp_file.txt")

    storage = KeyValueStorage(dict_file)
    assert storage._file_attrs == {}


def test_non_existing_file():
    with pytest.raises(ErrInDictFile) as err:
        KeyValueStorage("")
    assert "open" in str(err.value)


def test_wrong_format_without_equals(file_path):
    file_content = """name=kek
    last_name
    cnt=1"""
    dict_file = file_path(file_content, "tmp_file.txt")

    with pytest.raises(ErrInDictFile) as err:
        KeyValueStorage(dict_file)
    assert "wrong format" in str(err.value)


def test_write_attributes(file_path):
    file_content = """name=kek
    power=9001
    cnt=1"""
    dict_file = file_path(file_content, "tmp_file.txt")

    storage_step1 = KeyValueStorage(dict_file)
    assert storage_step1["power"] == 9001
    assert storage_step1["cnt"] == 1
    storage_step1.power = 9002
    storage_step1["cnt"] = 2
    storage_step1.save()
    del storage_step1

    storage_step2 = KeyValueStorage(dict_file)
    assert storage_step2["power"] == 9002
    assert storage_step2["cnt"] == 2
    storage_step2.power = 9001
    storage_step2["cnt"] = 1
    storage_step2.save()


# TODO: write tests for "one two" key
#  key ""
