import sqlite3


class TableData(object):
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
        self.conn = sqlite3.connect(db_path)
        self.table = table

    def __len__(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {self.table}")
        return cursor.fetchone()[0]

    def __contains__(self, item):
        ...

    def __iter__(self):
        ...

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    new_object = TableData("example.sqlite", "presidents")
    print(len(new_object))
