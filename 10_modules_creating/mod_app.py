'''
3h24m. We can import a module. This is to reuse and organise our code.
In this example we import mod_convert.py
'''


import mod_convert as cm #This imports everything
from mod_convert import kg2lbs #This imports one function/class


print(cm.kg2lbs(70))