#! /usr/bin/env python3

"""Необходимо создать 3 класса и взаимосвязь между ними.

(Student, Teacher, Homework).

Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и
количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и
    возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется
    сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
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


class Student:
    """A class to represent a student.

    Attributes:
        last_name (str): a last name of a student.
        first_name (str): a first name of a student.
    """

    def __init__(self, last_name: str, first_name: str) -> None:
        """Initialise a student with last_name and first_name.

        Args:
            last_name: a last name of a student.
            first_name: a first name of a student.
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Optional[Homework]:
        """Check if a homework is active or not.

        Receive a homework and returns it, if it is active,
        else if the task is outdated, then prints 'You are late'
        and returns None.

        Args:
            homework: a homework that should be done
                by the student.

        Returns:
            Returns the homework, if it is active, else if the task
            is outdated, then prints 'You are late' and returns None.
        """
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """A class to represent a teacher.

    Attributes:
        last_name (str): a last name of a teacher.
        first_name (str): a first name of a teacher.
    """

    def __init__(self, last_name: str, first_name: str) -> None:
        """Initialise a teacher with last_name and first_name.

        Args:
            last_name: a last name of a teacher.
            first_name: a first name of a teacher.
        """
        self.last_name = last_name
        self.first_name = first_name

    @classmethod
    def create_homework(cls, text: str, num_days: float) -> Homework:
        """Create a homework.

        Args:
            text: a task of a homework.
            num_days: number of days before the deadline.

        Returns:
            Homework: generated a homework.

        Example:
            expired_homework = \
                teacher.create_homework("Learn functions", 0)
            expired_homework.created
                # Example: 2019-05-26 16:44:30.688762
            expired_homework.deadline  # 0:00:00
            expired_homework.text  # 'Learn functions'
        """
        return Homework(text, num_days)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
