import os
import pytest

from homeworks.homework8.task1 import KeyValueStorage


def test_smoke():
    dict_file = (
        f"{os.path.dirname(__file__)}" "/test_data_task1/access_to_attribute.txt"
    )
    storage = KeyValueStorage(dict_file)
    assert "name" in storage.__dict__
    assert storage["name"] == "kek"


def test_access_to_attributes():
    dict_file = (
        f"{os.path.dirname(__file__)}" "/test_data_task1/access_to_attribute.txt"
    )
    storage = KeyValueStorage(dict_file)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage["power"] == 9001
    assert storage["song"] == "shadilay"
    assert storage["cnt"] == 1


def test_err_key():
    dict_file = f"{os.path.dirname(__file__)}" "/test_data_task1/err_key.txt"
    with pytest.raises(ValueError):
        storage = KeyValueStorage(dict_file)
        print(storage.__dict__)


def test_write_attributes():
    dict_file = f"{os.path.dirname(__file__)}" "/test_data_task1/write_step1.txt"

    storage_step1 = KeyValueStorage(dict_file)
    assert storage_step1["power"] == 9001
    assert storage_step1["cnt"] == 1
    storage_step1.power = 9002
    storage_step1["cnt"] = 2
    del storage_step1

    storage_step2 = KeyValueStorage(dict_file)
    assert storage_step2["power"] == 9002
    assert storage_step2["cnt"] == 2
    storage_step2.power = 9001
    storage_step2["cnt"] = 1


# TODO: write tests for "one two" key
#  key ""
#  line with multiple " =  = "
