from data_module2 import *

print(dir()) # notice there is __country, age, and name attribute that got imported as defined in the __all__ attribute of data_module2
# rest of the global scope names did not get imported when using from *.

# again we can still import any global name from a module using other import forms.
import data_module2
print(data_module2.city)
print(data_module2._aadhar_number)

