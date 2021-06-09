import sqlite3
from pathlib import Path

import pytest

from homeworks.homework8.task2 import TableData


@pytest.fixture
def db_path():
    return str(Path(__file__).parent / "test_data_task2/example.sqlite")


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
    with pytest.raises(KeyError):
        assert presidents["Y_e_l_t_s_i_n"]
        assert books["1_9_8_4"]


def test_contains(presidents, books):
    assert "Yeltsin" in presidents
    assert "Farenheit 451" in books
    assert "Y_e_l_t_s_i_n" not in presidents
    assert "F_a_r_e_n_h_e_i_t 451" not in books


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


def test_sql_table_in_ram():
    con = sqlite3.connect("file:cachedb?mode=memory&cache=shared")

    cur = con.cursor()
    cur.execute(
        """create table if not exists presidents
        (name varchar not null,
        age int not null,
        country varchar not null)"""
    )

    # This is the qmark style:
    cur.execute("insert into presidents values (?, ?, ?)", ("Yeltsin", 999, "Russia"))
    cur.execute("commit")

    presidents = TableData("file:cachedb?mode=memory&cache=shared", "presidents")
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")

    con.close()


def test_open_non_existing_database():
    with pytest.raises(sqlite3.OperationalError):
        return TableData("non_existing.sqlite", "presidents")
