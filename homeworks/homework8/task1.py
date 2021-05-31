from typing import Any, Dict


class KeyValueStorage:
    """A class for wrapping a key=value storage file.

    Each line of the file is represented as key and value separated
    by = symbol. Values can be strings or integer numbers. If a value
    can be treated both as a number and a string, it is treated as
    number. Its keys and values accessible as collection items and
    as attributes.

    Attributes:
        path (str): a path to a storage file.
        attr_dictionary (dict): a dictionary with attributes, read
            from the path.

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

    # TODO: use metaclass?
    def __init__(self, path: str):
        self.path = path
        self.attr_dictionary: Dict[str, Any] = dict()
        self._read_attributes()

        for key, value in self.attr_dictionary.items():
            # TODO: to analyse exception
            setattr(self, key, value)

    def _read_attributes(self):
        """Read attributes from path and add them to self."""
        with open(self.path) as fi:
            for line in fi:
                key, value = line.strip().split("=")
                if not key.isidentifier():
                    raise ValueError(
                        f"name '{key}' can't be an attribute for the " f"class "
                    )
                if value.isnumeric():
                    value = int(value)
                self.attr_dictionary[key] = value

    def _write_attributes(self):
        """Write attributes to path."""
        with open(self.path, "w") as fi:
            for key, value in self.attr_dictionary.items():
                fi.write(f"{key}={value}\n")

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        if key not in self.attr_dictionary:
            return
        self.attr_dictionary[key] = value
        self._write_attributes()

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if "attr_dictionary" not in self.__dict__:
            return
        self[key] = value
