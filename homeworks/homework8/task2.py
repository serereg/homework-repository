import sqlite3
from contextlib import contextmanager
from urllib.parse import parse_qs, urlparse


@contextmanager
def open_db(db_path: str, row_factory=None):
    conn = None
    try:
        conn = sqlite3.connect(f"{db_path}")
        if row_factory:
            conn.row_factory = row_factory
        cursor = conn.cursor()
        yield cursor
    finally:
        if conn:
            conn.close()


class TableData:
    """A wrapper class for database table.

    Object initializes with a database name and a table acts as a
    collection object (implements Collection protocol). All data must
    have unique values in 'name' column.

    Example:
        presidents = TableData(database_name='example.sqlite',\
            table_name='presidents')

        len(presidents)  # will give current amount of rows in
            presidents table in database
        presidents['Yeltsin']  # should return single data row for
            president with name Yeltsin
        'Yeltsin' in presidents  # should return if president with same
            name exists in table
        for president in presidents:
          print(president['name'])  # Iteration protocol implemented.
            You cac use it in for loops
    """

    def __init__(self, db_path: str, table: str):
        """Initialise object with database and table.

        Args:
            db_path: a path to the decorating database.
            table: a table to work with.
        """
        mode = parse_qs(urlparse(db_path)[4]).get("mode", [])

        self._db_path = db_path if "memory" in mode else (f"file:{db_path}?mode=rw")
        self._table = table

        with open_db(self._db_path) as cursor:
            cursor.execute(
                """SELECT name FROM sqlite_master
            WHERE type='table';"""
            )
            if table not in [existing_table[0] for existing_table in cursor.fetchall()]:
                raise ValueError(f"Not existing table {table}")

    def __len__(self):
        with open_db(self._db_path) as cursor:
            cursor.execute(f"select count(*) from {self._table}")
            return cursor.fetchone()[0]

    def __iter__(self):
        with open_db(self._db_path, sqlite3.Row) as cursor:
            for row in cursor.execute(f"select * from {self._table}"):
                yield dict(row)

    def __getitem__(self, item):
        with open_db(self._db_path) as cursor:
            cursor.execute(
                f"select * from {self._table} where name=:item", {"item": item}
            )
            if (response := cursor.fetchone()) is None:
                raise KeyError(f"Key {item} doesn't exist in a table {self._table}")
            return response

    def __contains__(self, item):
        try:
            return self[item] is not None
        except KeyError:
            return None
