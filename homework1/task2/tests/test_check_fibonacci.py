import pytest

from check_fibonacci.check_fibonacci import check_fibonacci

def test_empty_sequence():
    """Testing empty sequence"""
    assert not check_fibonacci([])
    
def test_first_3_sequence():
    """ """
    assert check_fibonacci([0])
    assert check_fibonacci([0, 1])
    assert check_fibonacci([0, 1, 1])    

def test_normal():
    """Testing that zero give False"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])    

#TODO: write test for 65536 (or biggest integer)

def test_last_number_of_sequence():
    """Testing all numbers are cheked """
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 7])