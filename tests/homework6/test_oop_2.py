from homework6.oop_2 import Homework, HomeworkResult, Student, Teacher


def test_creating_objects():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework = teacher.create_homework("Learn OOP", 1)
    homework_result = student.do_homework(homework, "I have done this hw")
    assert isinstance(teacher, Teacher)
    assert isinstance(student, Student)
    assert isinstance(homework, Homework)
    assert isinstance(homework_result, HomeworkResult)


# def test_homework_exception():
#     try:
#         HomeworkResult(good_student, "fff", "Solution")# type: ignore
#     except Exception:
#         print("There was an exception here")


def test_creating_resetting_homework_results_by_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework_1 = teacher.create_homework("Learn OOP", 1)
    homework_1_result = student.do_homework(homework_1, "I have done this hw")
    assert teacher.check_homework(homework_1_result) is True
    assert teacher.homework_done[homework_1] == homework_1_result

    homework_2 = teacher.create_homework("homework 2", 1)
    homework_2_result = student.do_homework(homework_2, "zero")
    assert teacher.check_homework(homework_2_result) is False
    assert teacher.homework_done.get(homework_2) is None

    assert len(teacher.homework_done) == 1
    Teacher.reset_results()
    assert len(teacher.homework_done) == 0


def test_all():
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
        HomeworkResult(good_student, "fff", "Solution")  # type: ignore
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
