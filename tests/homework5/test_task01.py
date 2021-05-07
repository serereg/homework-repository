import datetime

from homework5.oop_1 import Student, Teacher


def test_creating_objects():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    assert teacher.last_name == "Daniil"
    assert student.first_name == "Petrov"


def test_working_with_homework():
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    # expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    assert expired_homework.deadline == datetime.timedelta(0)
    assert expired_homework.text == "Learn functions"


def test_create_function_from_method_and_use_it():
    create_homework_too = Teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(days=5)
    # student.do_homework(oop_homework)
    # student.do_homework(expired_homework)  # You are late
