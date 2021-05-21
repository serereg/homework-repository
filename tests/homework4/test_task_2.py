from unittest.mock import Mock
import requests


from homeworks.homework4.task_2_mock_input import count_dots_on_i


def test_i_in_string(monkeypatch):
    get_mock = Mock()
    get_mock.return_value.text = "iii"
    monkeypatch.setattr(requests, "get", get_mock)

    assert count_dots_on_i("xxx.yy") == 3


def test_i_with_empty_string(monkeypatch):
    get_mock = Mock()
    get_mock.return_value.text = ""
    monkeypatch.setattr(requests, "get", get_mock)

    assert count_dots_on_i("xxx.yy") == 0
