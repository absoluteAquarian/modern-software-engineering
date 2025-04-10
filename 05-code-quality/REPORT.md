# Static and Dynamic Code Analysis Report

## Static Analysis

**pylint**:
- (lines 1, 2) Unused imports
- (lines 1, 5, 26) Missing docstrings for `import` statements and methods
- (lines 5, 21, 22) Function arguments and variables did not conform to the `snake_case` naming style
- (line 28) Unused variable in `main()` function's body
- (line 33) Newline missing at end of file

Code rating: _4.35/10_

**flake8**:
- (lines 1, 2) Unused imports
- (line 28) Local variable in `main()` is assigned to but never used
- (line 33) Missing newline at end of file

**mypy**:
- No issues found

## Line profiling

**line_profiler**:
- Excessive bottleneck found in `expensive_op()` after `@profile`ing each function
- Results:
  ```
  Total time: 0.689831 s
  File: main.py
  Function: expensive_op at line 4

  Line #      Hits         Time  Per Hit   % Time  Line Contents
  ==============================================================
       4                                           @profile
       5                                           def expensive_op(n):
       6      1000        324.3      0.3      0.0      total = 0
       7   1001000     312450.5      0.3     45.3      for i in range(1000):
       8   1000000     376735.1      0.4     54.6          total += i * n
       9      1000        321.4      0.3      0.0      return total
  ```
  ```
  Total time: 1.18898 s
  File: main.py
  Function: slow_func at line 11

  Line #      Hits         Time  Per Hit   % Time  Line Contents
  ==============================================================
      11                                           @profile
      12                                           def slow_func(lst):
      13         1          0.4      0.4      0.0      result = []
      14      1001        358.6      0.4      0.0      for i in range(len(lst)):
      15      1000    1188621.0   1188.6    100.0          result.append(expensive_op(i))
      16         1          0.6      0.6      0.0      return result
  ```
  ```
  Total time: 0 s
  File: main.py
  Function: unused_function at line 18

  Line #      Hits         Time  Per Hit   % Time  Line Contents
  ==============================================================
      18                                           @profile
      19                                           def unused_function():
      20                                               x = 10
      21                                               y = 20
      22                                               z = x + y
      23                                               return z
  ```
  ```
  Total time: 1.18981 s
  File: main.py
  Function: main at line 25

  Line #      Hits         Time  Per Hit   % Time  Line Contents
  ==============================================================
      25                                           @profile
      26                                           def main():
      27         1         10.8     10.8      0.0      numbers = list(range(1000))
      28         1    1189574.6    1e+06    100.0      output = slow_func(numbers)
      29         1        221.5    221.5      0.0      print("Done")
  ```

### Fix:
`expensive_op()` is effectively performing `result = n * (1 + 2 + ... + 999)`, which is a scalar multiplied by an arithmetic series.  
More specifically, the arithmetic series `S(n) = 1 + 2 + ... + n` is equivalent to `S(n) = n * (n + 1) / 2`.  
Hence, the function has been updated to use this reduced form instead of a loop:
```python
def expensive_op(n):
    return n * 999 * 1000 // 2
```
This, in turn, significantly reduced the time spent on the function when profiling.
```
Total time: 0.0003915 s
File: main.py
Function: expensive_op at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def expensive_op(n):
     6      1000        391.5      0.4    100.0      return n * 999 * 1000 // 2
```

## Code Coverage

## Fix Summary