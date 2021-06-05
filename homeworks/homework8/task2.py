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
        self._db_path = db_path
        self._table = table
        self._cursor_for_iterations: Optional[sqlite3.Cursor] = None

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        response = cursor.fetchall()
        if table not in [existing_table[0] for existing_table in response]:
            conn.close()
            raise ValueError(f"Not existing table {table}")
        conn.close()

    def __len__(self):
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        cursor.execute(f"select count(*) from {self._table}")
        response = cursor.fetchone()[0]
        conn.close()
        return response

    def __iter__(self):
        if self._cursor_for_iterations is None:
            self._conn = sqlite3.connect(self._db_path)
            self._conn.row_factory = sqlite3.Row
            self._cursor_for_iterations = self._conn.cursor()
            self._cursor_for_iterations.execute(f"select * from {self._table}")

        response = self._cursor_for_iterations.fetchone()

        while response:
            yield dict(response)
            response = self._cursor_for_iterations.fetchone()
        self._cursor_for_iterations = None
        self._conn.close()

    def __getitem__(self, item):
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        cursor.execute(f"select * from {self._table} where name=:item", {"item": item})
        response = cursor.fetchone()
        if response is None:
            conn.close()
            raise KeyError(f"Key {item} doesn't exist in a table {self._table}")
        conn.close()
        return response

    def __contains__(self, item):
        return self[item] is not None
