from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Student


class DBClient:
    def __init__(self, dsn, db):
        self.db = db
        self.dsn = dsn

    def connect(self):
        engine = create_engine(self.dsn)
        self.db.metadata.create_all(engine)

        self.db.metadata.bind = engine
        DBSession = sessionmaker()
        self.session = DBSession(bind=engine)

    def close(self):
        self.db.pop_bind().close()

    def create_student(self, last_name, first_name):
        student = Student(last_name=last_name, first_name=first_name)
        self.session.add(student)
        self.session.commit()
        return student
