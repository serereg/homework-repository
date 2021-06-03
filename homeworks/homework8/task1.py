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

    Attributes:
        path (str): a path to a storage file.
        _file_attrs (dict): a dictionary with attributes, read
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

    def __init__(self, path: str, prefix="prefix"):
        self._path = path
        self._prefix = prefix
        self._protected_attrs = dir(self)
        self._file_attrs = self._read_attributes(self._path)

        for key, value in self._file_attrs.items():
            setattr(self, key, value)

    @staticmethod
    def _read_attributes(path):
        """Read attributes from path and add them to self."""
        try:
            with open(path) as fi:
                # we assume the file is small
                lines = fi.readlines()
        except OSError as err:
            # https://stackoverflow.com/questions/9157210/how-do-i-raise
            # -the-same-exception-with-a-custom-message-in-python
            raise ErrInDictFile(f"Could not open/read file: {path}") from err

        attributes_from_file = {}
        for line in lines:
            try:
                key, value = line.strip().split("=", 1)
            except ValueError as err:
                raise ErrInDictFile(f"File {path}" f"has wrong format") from err

            if not key.isidentifier():
                raise ValueError(
                    f"name '{key}' can't be an attribute "  # fmt: off
                    f"for the class "  # fmt: on
                )
            if value.isnumeric():
                value = int(value)

            attributes_from_file[key] = value

        return attributes_from_file

    def save(self):
        """Write attributes to path."""
        # TODO: add exception
        with open(self._path, "w") as fi:
            for key, value in self._file_attrs.items():
                fi.write(f"{key}={value}\n")

    def __getitem__(self, item):
        if item not in self._file_attrs:
            raise KeyError(f"given a non existing key {item}")
        return getattr(self, item)

    def __setitem__(self, key, value):
        if key not in self._file_attrs:
            # raise KeyError(f"given a non existing key {item}")
            return
        self._file_attrs[key] = value

    def __setattr__(self, key, value):
        if hasattr(self, "_protected_attrs") and key in self._protected_attrs:
            key = f"{self._prefix}{key}"

        super().__setattr__(key, value)
        if not hasattr(self, "_file_attrs"):
            return
        self[key] = value
