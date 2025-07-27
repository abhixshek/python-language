import sys


a = sys.version_info # gives the major, minor, micro, release level info about the python version in use
print(a)
print(type(a))

# this can be compared with a tuple to establish that the python version running is what you want.
print(a >= (3, 9))
print(a >= (3, 10))
print(a >= (3, 9, 7))
print(a >= (3, 9, 6))
print(a >= (3, 9, 5))
print(a >= (3,)) # True if it is running python3 

# use the assert keyword to throw an AssertionError if the comparison is False
assert sys.version_info >= (3, 7) # does nothing if the assertion is true. program execution will continue.




