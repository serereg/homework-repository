from .db.client import DBClient

# from .db.fixtures import FIXTURES
# from .db.models import Base


def db_connect(dsn, db):
    client = DBClient(dsn=dsn, db=db)
    client.connect()
    return client
