#! /usr/bin/env python3

"""
Написать декоратор instances_counter, который применяется к
любому классу и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых
экземпляров класса reset_instances_counter - сбросить счетчик
экземпляров, возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""
    if any(
        map(
            lambda name: hasattr(cls, name),
            [
                "get_created_instances",
                "reset_instances_counter",
                "counter",
            ],
        )
    ):
        raise TypeError("Methods are already exists")

    cls.counter = 0

    def init_with_counter(func):
        def wrapper(*args, **kwargs):
            cls.counter += 1
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def get_created_instances(n_cls) -> int:
        print(n_cls.counter)
        return n_cls.counter

    @classmethod
    def reset_instances_counter(n_cls):
        saved_counter = n_cls.counter
        n_cls.counter = 0
        print(saved_counter)
        return saved_counter

    cls.__init__ = init_with_counter(cls.__init__)
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    def __init__(self):
        self.first = "first"


@instances_counter
class Admin:
    # counter = 1

    def __init__(self):
        self.first = "first"


if __name__ == "__main__":
    User.get_created_instances()  # type: ignore
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # type: ignore
    user.reset_instances_counter()  # type: ignore

    print(user.first)
    # admin = Admin()
