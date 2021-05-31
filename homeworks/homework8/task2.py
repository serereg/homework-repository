import sqlite3

from typing import Optional


class TableData:
    """A wrapper class for database table.

    Object initializes with database name and table acts as collection
    object (implements Collection protocol). All data must have unique
    values in 'name' column.

    db_path (str): a path to the decorating database
    table (str): name af decorating table

    Example:
        presidents = TableData(database_name='example.sqlite',\
            table_name='presidents')

        len(presidents)  # will give current amount of rows in
            presidents table in database
        presidents['Yeltsin']  # should return single data row for
            president with name Yeltsin
        'Yeltsin' in presidents  # should return if president with same
            name exists in table
    """

    def __init__(self, db_path: str, table: str):
        self._conn = sqlite3.connect(db_path)
        self._table = table
        self._cursor: Optional[sqlite3.Cursor] = None

    def __len__(self):
        cursor = self._conn.cursor()
        # TODO: change calls execute(...) to use with parameters
        cursor.execute(f"SELECT COUNT(*) FROM {self._table}")
        return cursor.fetchone()[0]

    def __contains__(self, item):
        cursor = self._conn.cursor()
        cursor.execute(f"SELECT * from {self._table} where name=:item", {"item": item})
        return cursor.fetchone() is not None

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor is None:
            self._cursor = self._conn.cursor()
            self._cursor.execute(f"SELECT * from {self._table}")

        columns = list(map(lambda x: x[0], self._cursor.description))
        response = self._cursor.fetchone()

        if response:
            dict_response = dict(zip(columns, response))
            return dict_response
        self._cursor = None
        raise StopIteration

    def __getitem__(self, item):
        cursor = self._conn.cursor()
        cursor.execute(f"SELECT * from {self._table} where name=:item", {"item": item})
        return cursor.fetchone()

    def __del__(self):
        self._conn.close()
