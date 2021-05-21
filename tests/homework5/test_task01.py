import datetime
import pytest

from homeworks.homework5.oop_1 import Homework, Student, Teacher

FAKE_TIME = datetime.datetime(2020, 12, 25, 17, 5, 55)


@pytest.fixture
def patch_datetime_now(monkeypatch):
    """
    Patches method datetime.datetime.now()
    """

    class MyDatetime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, "datetime", MyDatetime)


def test_creating_objects():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    assert teacher.last_name == "Daniil"
    assert student.first_name == "Petrov"


def test_creating_homework_by_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert isinstance(expired_homework, Homework)
    assert expired_homework.deadline == datetime.timedelta(0)
    assert expired_homework.text == "Learn functions"


def test_working_with_time_in_homework(patch_datetime_now):
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert expired_homework.created == FAKE_TIME
    assert expired_homework.deadline == datetime.timedelta(0)


def test_creating_function_from_method_and_using_it():
    create_homework_too = Teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(days=5)


def test_do_homework_with_expired_homework_and_not_expired(capsys):
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    oop_homework = teacher.create_homework("create 2 simple classes", 5)
    student = Student("Roman", "Petrov")
    student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out.strip() == "You are late"
    assert oop_homework == student.do_homework(oop_homework)
