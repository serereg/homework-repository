import functools
from homework5.save_original_info import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_with_error_at_the_begining(capsys):
    custom_sum([1, 2, 3], [4, 5])
    captured = capsys.readouterr()
    assert captured.out == "[1, 2, 3, 4, 5]\n"

    custom_sum(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out == "10\n"


def test_saving_original_functional_info():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"


def test_writing_original_function_pointer(capsys):
    print(custom_sum.__original_func)
    captured = capsys.readouterr()
    assert captured.out.startswith("<function custom_sum")
