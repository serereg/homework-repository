# import datetime
# from collections import defaultdict
from sqlalchemy import Column, ForeignKey, Integer, Interval, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from typing import Any  # noqa


class DeadLineError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


# https://github.com/python/mypy/issues/2477
Base = declarative_base()  # type: Any


class Common:
    id = Column(Integer, primary_key=True)


class Homework(Common, Base):  # ignore
    __tablename__ = "homework"
    text = Column(String(64), nullable=False)
    created = Column(DateTime, nullable=False)
    deadline = Column(Interval)


class Person(Common, Base):
    __tablename__ = "person"
    last_name = Column(String(64))
    first_name = Column(String(64))


class Student(Common, Base):
    __tablename__ = "student"
    last_name = Column(String(64))
    first_name = Column(String(64))


class HomeworkResult(Common, Base):
    __tablename__ = "homework_result"
    author = Column(Integer, ForeignKey(f"{Student.__tablename__}.id"), nullable=False)
    homework = Column(
        Integer, ForeignKey(f"{Homework.__tablename__}.id"), nullable=False
    )
    solution = Column(String(128))
    created = Column(DateTime, nullable=False)


# class Teacher(Person):
#     __tablename__ = "teacher"
#     homework_done = Column(Integer,
#       ForeignKey(f"{HomeworkResult.__tablename__}.id"))
