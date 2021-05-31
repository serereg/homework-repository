#! /usr/bin/env python3

"""
Task.

В этом задании будем улучшать нашу систему классов из задания прошлой
лекции (Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное
задание и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -
    выкинуть подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при
do_homework, а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late'
вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью
наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда
    поподают все HomeworkResult после успешного прохождения
    check_homework (нужно гаранитровать остутствие повторяющихся
    результатов по каждому заданию), группировать по экземплярам
    Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке
    if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает
    True если ответ студента больше 5 символов, так же при успешной
    проверке добавить в homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не
    передавать, то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить
ответственно - давать логичные подходящие имена.
"""
from __future__ import annotations

import datetime
from collections import defaultdict
from typing import Optional


class Homework:
    """A class to represent a homework.

    Attributes:
        text (str): text of the homework.
        created (datetime.datetime): a datetime of creating
            the homework.
        deadline (datetime.timedelta): number of days for
            the doing the homework.
    """

    def __init__(self, text: str, num_days: float) -> None:
        """Initialise a homework, and a deadline period.

        Args:
            text: text of the homework.
            num_days: number of days for the doing the homework.
        """
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=num_days)

    def is_active(self) -> bool:
        """Check if the homework is done.

        Returns:
            bool: True if homework's deadline is expired,
                False otherwise.
        """
        return datetime.datetime.now() - self.created < self.deadline


class DeadLineError(Exception):
    """A class exception for outdated homeworks.

    Args:
        msg (str): Human readable string describing the exception.

    Attributes:
        msg (str): Human readable string describing the exception.
    """

    def __init__(self, msg: str):
        """Initialize exception message with msg."""
        self.msg = msg


class Person:
    """A class to represent a person.

    Attributes:
        last_name (str): a last name of a person.
        first_name (str): a first name of a person.
    """

    def __init__(self, last_name: str, first_name: str) -> None:
        """Initialise a person with last_name and first_name.

        Args:
            last_name: a last name of a person.
            first_name: a first name of a person.
        """
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """A class to represent a student.

    The class inherits properties from the Person.
    """

    def do_homework(
        self, homework: Homework, solution: str
    ) -> Optional[HomeworkResult]:
        """Check if a homework is active or not.

        Args:
            homework: a homework that should be done
                by the student.
            solution: a text with solution of homework.

        Returns:
            Receive a homework and a solution and returns object of
            HomeworkResult, if homework is active,
            else if the task is outdated, then raises exception
            DeadLineError 'You are late' and returns None.

        Raises:
            DeadLineError: if homework is outdated.
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadLineError("You are late")
        return None


class HomeworkResult:
    """A class saves info about a homework, its author, its solution.

    Attributes:
        author (Student): an author of a homework.
        homework (Homework): a homework.
        solution (str): a solution of the homework.
        created (datetime.datetime): date and time of
            creating solution of homework.
    """

    def __init__(self, author: Student, homework: Homework, solution: str) -> None:
        """Add info to a homework.

        Args:
            author: author of a homework.
            homework: a homework with a task to solve.
            solution: a solution of the homework.

        Raises:
              TypeError: if the given homework is not Homework.
        """
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Teacher(Person):
    """A class to represent a teacher.

    The class inherits properties from the Person.

    Attributes:
        homework_done (defaultsect): journal, saves results
            of homeworks, groups results by a key homework.
    """

    CONST_CRITERIA_OF_HOMEWORK_DONE = 5
    homework_done: defaultdict = defaultdict(set)

    @classmethod
    def create_homework(cls, text: str, num_days: int) -> Homework:
        """Create a homework.

        Args:
            text: task of the homework.
            num_days: number of days before deadline.

        Returns:
            Homework: generated a homework.
        """
        return Homework(text, num_days)

    @classmethod
    def check_homework(cls, hw_result: Optional[HomeworkResult]) -> bool:
        """Check a homework with a criteria.

        Length of string with the solution should be bigger than
        CONST_CRITERIA_OF_HOMEWORK_DONE.

        Args:
            hw_result: homework with its author and a solution.

        Returns:
            bool: True if homework is done, False otherwise.
        """
        if not isinstance(hw_result, HomeworkResult):
            return False
        if len(hw_result.solution) >= cls.CONST_CRITERIA_OF_HOMEWORK_DONE:
            cls.homework_done[hw_result.homework].add(hw_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None) -> None:
        """Remove given homework from journal homework_done.

        Remove given homework from journal homework_done,
        if None is given, then clear homework_done.

        Args:
            homework: homework, that should be removed, or
                None if all journal should be cleared.
        """
        if isinstance(homework, Homework):
            del Teacher.homework_done[homework]
            return None
        cls.homework_done = defaultdict(set)
        return None


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")  # type: ignore
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
