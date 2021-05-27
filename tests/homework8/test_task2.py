import os

from homeworks.homework8.task2 import TableData


def test_smoke():
    db_path = os.path.dirname(__file__) + "/example.sqlite"
    new_object = TableData(db_path, "presidents")
    assert len(new_object) == 3
