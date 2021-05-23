import pytest

from homework6.counter import instances_counter


def test_adding_methods_to_class():
    class User:
        def __init__(self):
            self.first = "first"

    @instances_counter
    class UserModified(User):
        ...

    added_methods = {"counter", "get_created_instances", "reset_instances_counter"}
    methods_of_original_class = set(User.__dict__)
    methods_of_decorated_class = set(UserModified.__dict__)
    assert added_methods == methods_of_decorated_class.difference(
        methods_of_original_class
    )


def test_create_and_reset_instance_counter():
    class User:
        def __init__(self):
            self.first = "first"

    @instances_counter
    class UserModified(User):
        ...

    user, _, _ = UserModified(), UserModified(), UserModified()
    user_get_created_instances = user.get_created_instances()
    assert 3 == user_get_created_instances  # type: ignore
    user_reset_instances_counter = user.reset_instances_counter()
    assert 3 == user_reset_instances_counter  # type: ignore
    user_get_created_instances = user.get_created_instances()
    assert 0 == user_get_created_instances  # type: ignore


def test_if_methods_exist():
    with pytest.raises(TypeError, match=r"[Mm]ethods.*exist"):

        @instances_counter
        class User:
            def get_created_instances(self):
                ...
