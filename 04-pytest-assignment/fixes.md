This document lists the bugs from `program.py` and their fixes:
1) `divide_numbers(a, b)` does not support divisions by zero
    - Fix: if `b` is zero, return `nan` if `a` is zero, `-inf` if `a` is negative or `inf` if `a` is positive