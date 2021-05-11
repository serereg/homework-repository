from homework6.counter import instances_counter


def test_adding_methods_to_class():
    class User:
        def __init__(self):
            self.first = "first"

    @instances_counter
    class UserLong(User):
        ...

    assert {"counter", "get_created_instances", "reset_instances_counter"} == set(
        UserLong.__dict__
    ).difference(set(User.__dict__))


# @instances_counter
# class Admin:
#     # counter = 1
#
#     def __init__(self):
#         self.first = "first"
#
#
# if __name__ == "__main__":
#     User.get_created_instances()  # type: ignore
#     user, _, _ = User(), User(), User()
#     user.get_created_instances()  # type: ignore
#     user.reset_instances_counter()  # type: ignore
#
#     print(user.first)
#     # admin = Admin()
#
