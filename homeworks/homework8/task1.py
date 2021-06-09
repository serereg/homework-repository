from pathlib import Path
from typing import Any


class ErrInDictFile(Exception):
    # TODO: add user code: int
    ...


class KeyValueStorage:
    """A class for wrapping a key=value storage file.

    Each line of the file is represented as key and value separated
    by = symbol. Values can be strings or integer numbers. If a value
    can be treated both as a number and a string, it is treated as
    number. Its keys and values accessible as collection items and
    as attributes.
    In case of attribute clash existing built-in attributes take
    precedence, but access to attributes can be done via
    ["name attribute"].

    Attributes:
        path (str): a path to a storage file.

    Example:
        input_file.txt
            name=kek
            last_name=top
            song_name=shadilay
            power=9001

        >> storage = KeyValueStorage('path_to_file.txt')
        >> storage['name']  # will be string 'kek'
        >> storage.song_name  # will be 'shadilay'
        >> storage.power  # will be integer 9001
    """

    def __init__(self, path: str):
        self._path = Path(path)
        self._file_attrs = self._read_attributes(self._path)

    @staticmethod
    def _read_attributes(path: Path) -> dict:
        """Read attributes from path and add them to self.

        Args:
            path (str): path to a file with attrs.
        """
        if not path.is_file():
            raise ErrInDictFile(f"Could not open/read file: {path}")

        attributes_from_file = {}
        with path.open() as fi:
            for line in fi:
                key: str
                value: Any
                try:
                    key, value = line.strip().split("=", 1)
                except ValueError as err:
                    raise ErrInDictFile(
                        f"""File {path} has
 wrong format"""
                    ) from err

                if not key.isidentifier():
                    raise ValueError(
                        f"""name '{key}' can't be an
 attribute for the class """
                    )
                if value.isnumeric():
                    attributes_from_file[key] = int(value)
                else:
                    attributes_from_file[key] = value

        return attributes_from_file

    def save(self):
        """Write attributes to the path."""
        # TODO: add exception
        try:
            with self._path.open("w") as fi:
                for key, value in self._file_attrs.items():
                    fi.write(f"{key}={value}\n")
        except OSError as err:
            # https://stackoverflow.com/questions/9157210/how-do-i-raise
            # -the-same-exception-with-a-custom-message-in-python
            raise ErrInDictFile(
                f"""Could not open/write
 a file: {self._path}"""
            ) from err

    def __getitem__(self, item):
        if item in self._file_attrs:
            return self._file_attrs[item]
        raise KeyError(f"No key {item} in a file {self._path}")

    def __getattr__(self, item):
        if item in self._file_attrs:
            return self._file_attrs[item]
        raise AttributeError(f"No attribute in a file {self._path}")

    def __setitem__(self, key, value):
        if key in self._file_attrs:
            self._file_attrs[key] = value
            return
        raise KeyError(f"No key {key} in a file {self._path}")

    def __setattr__(self, key, value):
        if "_file_attrs" in dir(self):
            if key in self._file_attrs:
                self._file_attrs[key] = value
                return
        super().__setattr__(key, value)
