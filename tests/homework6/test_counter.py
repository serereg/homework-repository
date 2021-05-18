import pytest

from homework6.counter import instances_counter


def test_adding_methods_to_class():
    class User:
        def __init__(self):
            self.first = "first"

    @instances_counter
    class UserModified(User):
        ...

    assert {"counter", "get_created_instances", "reset_instances_counter"} == set(
        UserModified.__dict__
    ).difference(set(User.__dict__))


def test_create_and_reset_instance_counter():
    class User:
        def __init__(self):
            self.first = "first"

    @instances_counter
    class UserModified(User):
        ...

    user, _, _ = UserModified(), UserModified(), UserModified()
    assert 3 == user.get_created_instances()  # type: ignore
    assert 3 == user.reset_instances_counter()  # type: ignore
    assert 0 == user.get_created_instances()  # type: ignore


def test_if_methods_exist():
    with pytest.raises(TypeError, match=r"[Mm]ethods.*exist"):

        @instances_counter
        class User:
            def get_created_instances(self):
                ...
