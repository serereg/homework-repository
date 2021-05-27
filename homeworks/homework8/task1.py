class KeyValueStorage:
    """A class for wrapping a key=value storage file.

    Each line of the file is represented as key and value separated
    by = symbol. Values can be strings or integer numbers. If a value
    can be treated both as a number and a string, it is treated as
    number. Its keys and values accessible as collection items and
    as attributes.

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

    # TODO: use metaclass?
    def __init__(self, path: str):
        self.path = path
        internal_dictionary = dict()
        with open(path) as fi:
            for line in fi:
                key, value = line.strip().split("=")
                internal_dictionary[key] = value

        for key, value in internal_dictionary.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == "__main__":
    new_object = KeyValueStorage("task1.txt")
    print(new_object.__dict__)
    print(new_object["name"])
