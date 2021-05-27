import os

from homeworks.homework8.task2 import TableData


def test_len():
    db_path = os.path.dirname(__file__) + "/example.sqlite"
    presidents = TableData(db_path, "presidents")
    assert len(presidents) == 3


def test_contains():
    db_path = os.path.dirname(__file__) + "/example.sqlite"
    presidents = TableData(db_path, "presidents")
    assert "Yeltsin" in presidents
