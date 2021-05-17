#! /usr/bin/env python3
"""
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
    """A class to represent a homework"""

    def __init__(self, text: str, num_days: float) -> None:
        """Initialise homework, and deadline period
        text: text of the homework
        deadline: datetime.timedelta - with number of days for
        the doing the homework
        created: datetime.datetime - datetime of creating homework
        """
        self.text = text
        self.num_days = num_days
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=num_days)

    def is_active(self) -> bool:
        """A method checks if the homework is done"""
        return datetime.datetime.now() - self.created < self.deadline


class DeadLineError(Exception):
    """A class exception for outdated homeworks"""

    def __init__(self, msg):
        """Initialize exception message with msg"""
        self.msg = msg


class Man:
    """A class to represent a man"""

    def __init__(self, last_name: str, first_name: str) -> None:
        """Initialise a man with last_name and first_name"""
        self.last_name = last_name
        self.first_name = first_name


class Student(Man):
    """A class to represent a student"""

    def do_homework(
        self, homework: Homework, solution: str
    ) -> Optional[HomeworkResult]:
        """Receives a homework and solution,
        returns object of HomeworkResult if the homework is active.
        Else if task is outdated, then raise an exception DeadLineError
        with 'You are late'
        and returns None
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadLineError("You are late")
        return None


class HomeworkResult:
    """A class saves info about homework, its author, its solution"""

    def __init__(self, author: Student, homework: Homework, solution: str) -> None:
        """Initializes results of homework with author,
        task of homework and solution"""
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Teacher(Man):
    """A class to represent a teacher"""

    CONST_CRITERIA_OF_HOMEWORK_DONE = 5
    homework_done: defaultdict = defaultdict()

    @classmethod
    def create_homework(cls, text: str, num_days: int) -> Homework:
        """A method creates homework
        text - task of the homework
        num_days - number of days before deadline
        """
        return Homework(text, num_days)

    def check_homework(self, home_result: Optional[HomeworkResult]) -> bool:
        """A method checks homework with criteria: len of the solution
        should be bigger than CONST_CRITERIA_OF_HOMEWORK_DONE
        text - task of the homework
        num_days - number of days before deadline
        """
        if not isinstance(home_result, HomeworkResult):
            return False
        if len(home_result.solution) >= Teacher.CONST_CRITERIA_OF_HOMEWORK_DONE:
            # TODO: to analise possible duplicates
            Teacher.homework_done[home_result.homework] = home_result
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None) -> None:
        """Removes given homework from journal homework_done,
        if None is given, then clears homework_done"""
        if isinstance(homework, Homework):
            del Teacher.homework_done[homework]
        Teacher.homework_done = defaultdict(list)


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
