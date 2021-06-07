"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


@contextmanager
def suppressor(err):
    """Suppress passed exception.

    A context manager, that suppresses passed exception.

    Example:
        >>> with suppressor(IndexError):
        ... [][2]
    """
    try:
        yield
    except err:
        pass
    finally:
        pass


class Suppressor(object):
    """A context manager, that suppresses passed exception.

    Example:
        >>> with suppressor(IndexError):
        ... [][2]
    """

    def __init__(self, err):
        self.err = err

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.err is exc_type:
            return True
