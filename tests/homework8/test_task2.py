import pytest
import os

from homeworks.homework8.task2 import TableData


@pytest.fixture
def db_path():
    return os.path.dirname(__file__) + "/test_data_task2/example.sqlite"


@pytest.fixture
def presidents(db_path):
    return TableData(db_path, "presidents")


@pytest.fixture
def books(db_path):
    return TableData(db_path, "books")


def test_len(presidents, books):
    assert len(presidents) == 3
    assert len(books) == 3


def test_getitem(presidents, books):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert books["1984"] == ("1984", "Orwell")


def test_contains(presidents, books):
    assert "Yeltsin" in presidents
    assert "Farenheit 451" in books


def test_iterators_in_for_loop(presidents, books):
    presidents_names = set()
    for president in presidents:
        presidents_names.add(president["name"])
    assert presidents_names == {"Yeltsin", "Trump", "Big Man Tyrone"}

    books_names = set()
    for book in books:
        books_names.add(book["author"])
    assert books_names == {"Bradbury", "Huxley", "Orwell"}


def test_iterators_in_several_calls_for_loops(presidents):
    presidents_names = set()
    for president in presidents:
        presidents_names.add(president["name"])
    assert presidents_names == {"Yeltsin", "Trump", "Big Man Tyrone"}

    presidents_names = set()
    for president in presidents:
        presidents_names.add(president["name"])
    assert presidents_names == {"Yeltsin", "Trump", "Big Man Tyrone"}
