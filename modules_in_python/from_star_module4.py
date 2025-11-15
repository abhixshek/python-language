from module1 import *


printer('imported everything at the top level of the referenced module')

print(r) # r was initialized in module1's global scope and so just like the function printer, r is also available because we imported everything from module1's global scope.

