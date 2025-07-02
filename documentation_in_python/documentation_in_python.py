# denote comments
a = 5 # comments are only visible in the source file

# dir() function lists all attributes available in an object
import sys
print(dir(sys))

print()
print(dir([])) # attributes of a list object
print()
print(dir('spam'))

print()
print(dir(int))

import docstrings
print('\nBelow is the docstrings of the docstrings.py module you wrote')
print(docstrings.__doc__)
print('\nBelow is the docstrins of the square function in the docstrings module you wrote')
print(docstrings.square.__doc__)
print()
print(docstrings.Employee.__doc__)

# python's help() built-in uses the PyDoc standard library and the object's __doc__ attribute 

help(docstrings.square) # prints the function header and the docstring that you provided for it.

help(docstrings) # the module we imported above
import sys
help(sys.getrefcount)

help(str)


