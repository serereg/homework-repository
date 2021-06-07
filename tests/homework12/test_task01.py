from homeworks.homework12.task01 import db_connect
from homeworks.homework12.db.models import Base
import os


def test_smoke():
    db_connect(f"sqlite:///{os.path.dirname(__file__)}/db/db.sqlite3", Base)
    assert True
