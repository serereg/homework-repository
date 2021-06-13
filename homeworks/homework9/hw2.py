"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager
from typing import Any, Iterator


@contextmanager
def suppressor(*args) -> Iterator[None]:
    """Suppress passed exception.

    A context manager, that suppresses passed exception.

    Example:
        >>> with suppressor(IndexError):
        ... [][2]
    """
    try:
        yield
    except args:
        pass


class Suppressor(object):
    """A context manager, that suppresses passed exception.

    Example:
        >>> with suppressor(IndexError):
        ... [][2]
    """

    def __init__(self, *args):
        """Initialise suppressed exception.

        Args:
            err: type of suppressed exception, like ValueError etc.
        """
        self._err = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, exc_traceback: Any) -> bool:
        if exc_type in self._err:
            return True
        return False
