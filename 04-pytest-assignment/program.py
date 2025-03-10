def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""

    # 0/0 is undefined, +X/0 is +inf and -X/0 is -inf
    if b == 0:
        if a == 0:
            return float('nan')
        elif a < 0:
            return float('-inf')
        else:
            return float('inf')

    result = a / b
    return round(result, 2)


def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""

    if not isinstance(s, str):
        raise TypeError('Argument must be a str')

    reversed_s = s[::-1]
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case


def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not found' if out of range."""
    if index < len(lst):  # Bug: Incorrect boundary check
        return lst[index]
    else:
        return "Not found"  # Bug: Should probably raise an exception instead