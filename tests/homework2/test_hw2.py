from homework2.hw2 import major_and_minor_elem


def test_of_one_elem():
    """Testing when given list with one element"""
    assert 20, 20 == major_and_minor_elem([20])


def test_on_usual_list():
    """Testing when given usual list
    Input: [2,2,1,1,1,2,2]
    Output: 2, 1
    """
    assert 2, 1 == major_and_minor_elem([2, 2, 1, 1, 1, 2, 2])


# TODO: test on empty list
