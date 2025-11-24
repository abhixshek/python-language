from data_module import *
# although from * form imports all attributes available in the global scope of that module, it does not import names starting with an _


print(dir()) # dir() without arguments shows all variable names available in the scope it is called in.
# notice in this list, there is no _aadhar_number
# there is also no __country

print('_aadhar_number' in dir())
print('name' in dir())

# you can still import names starting with underscores using other import statement forms
from data_module import _aadhar_number
print(_aadhar_number)

import data_module
print(data_module._aadhar_number)
print(data_module.__country)


