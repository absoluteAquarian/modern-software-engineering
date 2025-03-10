import pytest
from program import divide_numbers, reverse_string, get_list_element


def test_divide_numbers():
    assert divide_numbers(10, 3) == 3.33