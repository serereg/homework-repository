from homeworks.homework4.task_3_get_print_output import my_precious_logger


def test_with_error_at_the_begining(capsys):
    text = "eRror: some info"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert (captured.out, captured.err) == ("", f"{text}")


def test_without_error_at_the_begining(capsys):
    text = ":error nothing important"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert (captured.out, captured.err) == (f"{text}", "")
