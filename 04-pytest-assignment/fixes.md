This document lists the bugs from `program.py` and their fixes:
1) `divide_numbers(a, b)` does not support divisions by zero
    - Fix: if `b` is zero, return `nan` if `a` is zero, `-inf` if `a` is negative or `inf` if `a` is positive
2) `reverse_string` uses the slice operator (`obj[start:stop:step]`) to reverse the string, but the operator also works on non-`str` objects
    - Fix: using an `isinstance(s, str)` call, a `TypeError` is raised if `s` is not a `str`
3) `get_list_element` had incomplete bounds checking
    - Fix: `index < len(lst)` was replaced with `0 <= index < len(lst)`
4) `get_list_element` returned `"Not found"` if `index` was out of range rather than raising an error
    - Fix: `return "Not found"` was replaced with `raise IndexError()`