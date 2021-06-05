import sqlite3


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
        self._db_path = db_path
        self._table = table

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
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(f"select * from {self._table}")
        response = cursor.fetchone()
        while response:
            yield dict(response)
            response = cursor.fetchone()
        conn.close()

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
