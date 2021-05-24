from homework7.hw2 import backspace_compare


def test_equal_strings():
    assert backspace_compare("asfd sfd fd 123", "asfd sfd fd 123") is True
    assert backspace_compare("12344#56", "1222##3456") is True


def test_empty_strings():
    assert backspace_compare("####", "##") is True
    assert backspace_compare("", "") is True
    assert backspace_compare("12##", "1234####") is True


def test_non_equal_strings():
    assert backspace_compare("1234", "12") is False
    assert backspace_compare("12", "1234") is False
