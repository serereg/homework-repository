import pytest

from homework6.oop_2 import DeadLineError, Homework, HomeworkResult, Student, Teacher


def test_creating_objects():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework = teacher.create_homework("Learn OOP", 1)
    homework_result = student.do_homework(homework, "I have done this hw")
    assert isinstance(teacher, Teacher)
    assert isinstance(student, Student)
    assert isinstance(homework, Homework)
    assert isinstance(homework_result, HomeworkResult)


def test_do_homework_exception():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Lev", "Sokolov")
    homework = teacher.create_homework("Learn OOP", 0)
    with pytest.raises(DeadLineError, match=r"You are late"):
        student.do_homework(homework, "I have done this hw")


def test_creating_and_resetting_homework_results_by_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework_1 = teacher.create_homework("Learn OOP", 1)
    homework_1_result = student.do_homework(homework_1, "I have done this hw")
    assert teacher.check_homework(homework_1_result) is True
    assert homework_1_result in teacher.homework_done[homework_1]

    homework_2 = teacher.create_homework("homework 2", 1)
    homework_2_result = student.do_homework(homework_2, "zero")
    assert teacher.check_homework(homework_2_result) is False
    assert teacher.homework_done.get(homework_2) is None

    homework_3 = teacher.create_homework("homework 3", 1)
    homework_3_result = student.do_homework(homework_3, "I have done this hw")
    assert teacher.check_homework(homework_3_result) is True
    assert homework_3_result in teacher.homework_done.get(homework_3)

    assert len(teacher.homework_done) == 2
    Teacher.reset_results(homework_3)
    assert len(teacher.homework_done) == 1
    Teacher.reset_results()
    assert len(teacher.homework_done) == 0
