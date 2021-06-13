import pytest

from homeworks.homework9.hw2 import suppressor, Suppressor


class TestGenSuppressor:
    def test_suppress_wrong_exception(self):
        with pytest.raises(IndexError):
            with suppressor(ValueError):
                raise IndexError

    def test_suppress_right_exception(self):
        with suppressor(IndexError):
            raise IndexError
        assert True

    def test_suppress_no_exception(self):
        with suppressor(ValueError):
            pass

    def test_suppress_several_exceptions(self):
        with suppressor(IndexError, ValueError):
            raise IndexError
        with suppressor(IndexError, ValueError):
            raise ValueError
        assert True


class TestClassSuppressor:
    def test_suppress_wrong_exception(self):
        with pytest.raises(IndexError):
            with Suppressor(ValueError):
                raise IndexError

    def test_suppress_right_exception(self):
        with Suppressor(IndexError):
            raise IndexError
        assert True

    def test_suppress_no_exception(self):
        with Suppressor(ValueError):
            pass

    def test_suppress_several_exceptions(self):
        with Suppressor(IndexError, ValueError):
            raise IndexError
        with Suppressor(IndexError, ValueError):
            raise ValueError
        assert True
