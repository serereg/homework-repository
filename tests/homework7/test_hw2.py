from homework7.hw2 import backspace_compare


def test_equal_strings():
    result = backspace_compare("asfd sfd fd 123", "asfd sfd fd 123")
    assert result is True
    result = backspace_compare("12344#56", "1222##3456")
    assert result is True
    result = backspace_compare("#12344#56", "1222##3456")
    assert result is True


def test_empty_strings():
    result = backspace_compare("####", "##")
    assert result is True
    result = backspace_compare("", "")
    assert result is True
    result = backspace_compare("12##", "1234####")
    assert result is True


def test_non_equal_strings():
    result = backspace_compare("1234", "12")
    assert result is False
    result = backspace_compare("12", "1234")
    assert result is False
    result = backspace_compare("a", "ba")
    assert result is False
    result = backspace_compare("ba", "a")
    assert result is False
