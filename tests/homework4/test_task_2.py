from unittest.mock import Mock
import requests


# from homework4.task_2 import count_dots_on_i
def count_dots_on_i(url: str) -> int:
    text = requests.get(url).text
    return text.count("i")


def test_counts_dots_on_i(monkeypatch):
    request_mock = Mock()
    request_mock.get.return_value.text = "iii"
    monkeypatch.setitem(globals(), "requests", request_mock)

    assert count_dots_on_i("xxx.yy") == 3
