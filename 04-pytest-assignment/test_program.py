import pytest
from program import divide_numbers, reverse_string, get_list_element
import math

def test_divide_numbers():
    assert divide_numbers(10, 3) == 3.33

def test_divide_numbers_zero():
    assert divide_numbers(1, 0) == float('inf')

def test_divide_numbers_zero_zero():
    assert math.isnan(divide_numbers(0, 0))

def test_reverse_string():
    assert reverse_string("Hello World") == "DLROw OLLEh"

def test_reverse_string_not_string():
    with pytest.raises(TypeError) as excinfo:
        reverse_string(5)
    assert str(excinfo.value) == 'Argument must be a str'

def test_reverse_string_empty_string():
    assert reverse_string('') == ''

def test_get_list_element():
    lst = [ 1, 3, 5, 7, 9 ]
    assert get_list_element(lst, 1) == 3

def test_get_list_element_negative():
    lst = [ 1, 3, 5, 7, 9 ]
    pytest.raises(IndexError, get_list_element, lst, -1)

def test_get_list_element_too_large():
    lst = [ 1, 3, 5, 7, 9 ]
    pytest.raises(IndexError, get_list_element, lst, 5)