import os

from homeworks.homework8.task1 import KeyValueStorage


def test_smoke():
    dict_file = os.path.dirname(__file__) + "/task1.txt"
    new_object = KeyValueStorage(dict_file)
    print(new_object.__dict__)
    assert "name" in new_object.__dict__
    assert new_object["name"] == "kek"
