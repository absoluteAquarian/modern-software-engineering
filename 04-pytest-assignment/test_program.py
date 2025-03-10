import pytest
from program import divide_numbers, reverse_string, get_list_element
import math

def test_divide_numbers():
    assert divide_numbers(10, 3) == 3.33

def test_divide_numbers_zero():
    assert divide_numbers(1, 0) == float('inf')

def test_divide_numbers_zero_zero():
    assert math.isnan(divide_numbers(0, 0))