'''
Testing different types of exceptions 
'''

divisionlist = [10,9,8,7,6,5,4,3,2,1,0]
x = input('divide by: ')

try:
    for number in divisionlist:
        print(number / int(x))
except ZeroDivisionError: #Exception for the division by 0 error
    print('Cannot divide by 0')
except ValueError:
    print('Caanot divide by non numerical')


'''
Other common types
| **Number** | **Exception**                         | **Typical Context**            | **Example / Cause**            |
| -------- | ------------------------------------- | ------------------------------ | ------------------------------ |
| 1        | `ValueError`                          | Invalid value for an operation | `int("abc")`                   |
| 2        | `TypeError`                           | Wrong data type passed         | `len(5)`                       |
| 3        | `KeyError`                            | Missing dictionary key         | `d["not_found"]`               |
| 4        | `IndexError`                          | List/tuple index out of range  | `[1, 2][3]`                    |
| 5        | `AttributeError`                      | Accessing missing attribute    | `"str".not_exist`              |
| 6        | `NameError`                           | Undefined variable             | `print(x)` before `x` defined  |
| 7        | `ZeroDivisionError`                   | Division by zero               | `1 / 0`                        |
| 8        | `FileNotFoundError`                   | File path invalid or missing   | `open("missing.txt")`          |
| 9        | `OSError`                             | System-level or file I/O issue | Disk/network errors            |
| 10       | `Im
portError` / `ModuleNotFoundError` | Missing library/module         | `import not_real_lib`          |
| 11       | `RuntimeError`                        | Generic runtime failure        | Raised manually in code logic  |
| 12       | `AssertionError`                      | Failed `assert` statement      | `assert x > 0`                 |
| 13       | `StopIteration`                       | Iterator/generator finished    | Used internally by loops       |
| 14       | `TimeoutError`                        | Network or subprocess timeout  | `socket` or `subprocess` calls |
| 15       | `PermissionError`                     | Insufficient OS permissions    | Writing to protected dir       |

'''