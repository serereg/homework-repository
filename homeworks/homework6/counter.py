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


def instances_counter(prefix: str = ""):
    """Decorate class by adding methods for counting instances.

    Add methods 'get_created_instances',
    'reset_instances_counter' and '_count' attribute to the class.

    Args:
        prefix: you may add prefix to names of methods, in case
            decorated class already has one or them, i.e.
            pref_get_created_instances,
            pref_reset_instances_counter,
            _pref_count.

    Returns:
        A decorated class.

    Raises:
        TypeError: If any of the methods already exists.
    """

    def instances_counter_inner(cls):
        name_get_method = f"{prefix}get_created_instances"
        name_reset_method = f"{prefix}reset_instances_counter"
        name_counter_attr = f"_{prefix}counter"

        for name in (name_get_method, name_reset_method, name_counter_attr):
            if name in cls.__dict__:
                raise TypeError(f"The method {name} already exists")

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

    return instances_counter_inner


@instances_counter()
class User:
    def __init__(self):
        self.first = "first"


@instances_counter()
class Admin:
    def __init__(self):
        self.first = "first"


if __name__ == "__main__":
    User.get_created_instances()  # type: ignore
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # type: ignore
    user.reset_instances_counter()  # type: ignore

    print(user.first)
    # admin = Admin()
