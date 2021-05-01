from homework4.task_3_get_print_output import my_precious_logger


# TODO: 'error' in the begining
# :error - not in the begining
# without any error
# ErRor in the begining
# the output text is only in one direction out or err


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
