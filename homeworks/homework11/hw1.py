"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):  # is a metaclass
    """Return a class with attributes from a __keys attribute.

    Example:
        class ColorsEnum(metaclass=SimplifiedEnum):
            __keys = ("RED", "BLUE", "ORANGE", "BLACK")


        class SizesEnum(metaclass=SimplifiedEnum):
            __keys = ("XL", "L", "M", "S", "XS")


        assert ColorsEnum.RED == "RED"
        assert SizesEnum.XL == "XL"
    """

    def __new__(cls, name, bases, dct):
        cls_instance = super().__new__(cls, name, bases, dct)
        try:
            attrs = [*dct[f"_{cls_instance.__name__}__keys"]]
            for attr in attrs:
                setattr(cls_instance, attr, attr)
            return cls_instance
        except KeyError as k:
            raise KeyError("Class must have __key attribute") from k
