import pytest

from homeworks.homework11.hw1 import SimplifiedEnum


def test_smoke():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"


def test_non_existing_attribute():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    with pytest.raises(AttributeError):
        ColorsEnum.Noname == ""


def test_without_key_attribute():
    with pytest.raises(KeyError) as excinfo:

        class ColorsEnum(metaclass=SimplifiedEnum):
            pass

    assert "__key" in str(excinfo.value)
