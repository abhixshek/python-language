X = 99
def selector(): # X used but not assigned
    print(X) # X found in the global scope

selector() # prints 99

"""
X = 99
def selector():
    print(X)
    X = 88 # this code throws an error that X is referenced before assignment.
    # it is because during compile time Python sees the X = 88 assignment statement and treats X as a local name,
    # now during runtime, you happen to reference X thinking it will pick the global X but no Python has already categorized X as a local name
    # and you are referencing it before X has got any value assigned to it. and hence the error.

selector()
"""

# if you really meant to use the global X then declare it global first
X = 99
def selector():
    global X
    print(X)
    X = 88

selector() # prints 99
print(X) # prints 88. global X got updated too when you assigned X in the function

# if you really meant to print the global X and set a local X to 88 then you would have to import the same module and access the global X from there
X = 100
def selector():
    import function_gotchas
    print(function_gotchas.X)
    X = 88
    print(X)

selector() # prints 100
print(X) # prints 100. only local X was changed to 88 and that is not known outside the function

# the output when you run this module file:
"""
99
99
88
99
99
88
100
88
100
100
88
100
"""
# NOTE this code looks like would run infinitely but it does not, because Python does not import a module twice as imports are expensive operation
# once a module is loaded once, the import statement run again will not execute the code of that module. in fact it wont do anything the 2nd time.


