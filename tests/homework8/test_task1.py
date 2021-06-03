import os
import pytest

from homeworks.homework8.task1 import KeyValueStorage, ErrInDictFile


def test_smoke():
    dict_file = f"{os.path.dirname(__file__)}/test_data_task1/access_to_attribute.txt"
    storage = KeyValueStorage(dict_file)
    assert "name" in storage.__dict__
    assert storage["name"] == "kek"


def test_access_to_attributes():
    dict_file = f"{os.path.dirname(__file__)}/test_data_task1/access_to_attribute.txt"
    storage = KeyValueStorage(dict_file)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage["power"] == 9001
    assert storage["song"] == "shadilay"
    assert storage["cnt"] == 1


def test_access_to_non_exesting_attributes():
    dict_file = f"{os.path.dirname(__file__)}/test_data_task1/access_to_attribute.txt"
    storage = KeyValueStorage(dict_file)
    assert storage["name"] == "kek"
    with pytest.raises(KeyError) as err:
        storage["wrong"] == 1
    assert "key" in str(err.value)


def test_err_key():
    dict_file = f"{os.path.dirname(__file__)}/test_data_task1/err_key.txt"
    with pytest.raises(ValueError):
        storage = KeyValueStorage(dict_file)
        print(storage.__dict__)


def test_write_attributes():
    dict_file = f"{os.path.dirname(__file__)}/test_data_task1/write_step1.txt"

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


def test_non_existing_file():
    with pytest.raises(ErrInDictFile) as err:
        KeyValueStorage("")
    assert "open" in str(err.value)


def test_wrong_format_without_equals():
    dict_file = (
        f"{os.path.dirname(__file__)}/test_data_task1/err_format_without_equals.txt"
    )
    with pytest.raises(ErrInDictFile) as err:
        storage = KeyValueStorage(dict_file)
        print(storage.__dict__)
    assert "wrong format" in str(err.value)


# TODO: write tests for "one two" key
#  key ""
#  line with multiple " =  = "
