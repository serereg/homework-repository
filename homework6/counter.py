#! /usr/bin/env python3

"""
Task.

Написать декоратор instances_counter, который применяется к
любому классу и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых
экземпляров класса reset_instances_counter - сбросить счетчик
экземпляров, возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Decorate class by adding methods.

    Add methods get_created_instances,
    reset_instances_counter and _count attribute to the class.

    Returns:
        A decorated class.

    Raises:
        TypeError: If the methods are already exist.
    """
    # TODO: can add {prefix} to the names of
    #  adding methods and attributes,
    #  but the signature of the decorator will be changed,
    #  cause we need parametrised decorator (prefix)
    #  not @instances_counter, but @instances_counter(prefix='_')

    name_get_method = "get_created_instances"
    name_reset_method = "reset_instances_counter"
    name_counter_attr = "_counter"

    if any(
        k in cls.__dict__
        for k in (name_get_method, name_reset_method, name_counter_attr)
    ):
        raise TypeError("Methods are already exist")

    setattr(cls, name_counter_attr, 0)

    def init_with_counter(orig_init):
        def wrapper(*args, **kwargs):
            counter = getattr(cls, name_counter_attr)
            setattr(cls, name_counter_attr, counter + 1)
            return orig_init(*args, **kwargs)

        return wrapper

    @classmethod
    def get_created_instances(n_cls) -> int:
        return getattr(n_cls, name_counter_attr)

    @classmethod
    def reset_instances_counter(n_cls):
        saved_counter = getattr(n_cls, name_counter_attr)
        setattr(n_cls, name_counter_attr, 0)
        return saved_counter

    cls.__init__ = init_with_counter(cls.__init__)
    setattr(cls, name_get_method, get_created_instances)
    setattr(cls, name_reset_method, reset_instances_counter)
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
