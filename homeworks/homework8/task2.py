import sqlite3

from typing import Optional


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
        # _conn (sqlite3.Connection): a connection to the database.
        # _cursor (sqlite3.Cursor): internal cursor for the connection,
        #     for iterating over rows in the response.
        # _table (str): name af decorating table.

        self._conn = sqlite3.connect(db_path)
        self._table = table
        self._cursor: Optional[sqlite3.Cursor] = None

    def __len__(self):
        cursor = self._conn.cursor()
        # TODO: can't add self._table as parameter to a query
        cursor.execute(f"select count(*) from {self._table}")
        return cursor.fetchone()[0]

    def __contains__(self, item):
        cursor = self._conn.cursor()
        # TODO: can't add self._table as parameter to a query
        cursor.execute(f"select * from {self._table} where name=:item", {"item": item})
        return cursor.fetchone() is not None

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor is None:
            self._cursor = self._conn.cursor()
            # TODO: can't add self._table as parameter to a query
            self._cursor.execute(f"select * from {self._table}")

        columns_names = list(map(lambda x: x[0], self._cursor.description))
        response = self._cursor.fetchone()

        if response:
            return dict(zip(columns_names, response))
        self._cursor = None
        raise StopIteration

    def __getitem__(self, item):
        cursor = self._conn.cursor()
        # TODO: can't add self._table as parameter to a query
        cursor.execute(f"select * from {self._table} where name=:item", {"item": item})
        return cursor.fetchone()

    def __del__(self):
        self._conn.close()
