def times(a, b): # function header.
    return a * b
# a function object is created by the above def statement and assigned to the name times
r = times(5, 4) # function call
print(r)
r = times('spam', 4)
print(r) # spamspamspamspam

# our function works with more string and number objects for argument a. this allows it do perform repetition on strings and multiplication on numbers
# this is a key idea to using python well and is called polymorphism.

multiplier = times # you can assign new names that reference the name function object
r = multiplier(3, 8)
print(r)

# function to find out the common items in sequences (characters in strings)
def intersect(seq1, seq2):
    result = [] # start empty
    for item in seq1: # scan seq1
        if item in seq2: # common item?
            result.append(item) # add to end

    return result

s1 = 'spam'
s2 = 'scam'
r = intersect(s1, s2)
print(r) # ['s', 'a', 'm']

s1 = 'school'
s2 = 'college'
r = intersect(s1, s2)
print(r) # ['c', 'o', 'o', 'l']

# To be fair, our intersect function is fairly slow (it executes nested loops), isn’t really
# mathematical intersection (there may be duplicates in the result), and isn’t required at
# all (as we’ve seen, Python’s set data type provides a built-in intersection operation).

def intersect(seq1, seq2):
    # this is shorted to code and better but its still nested loops
    # recall in operator is implicitly doing a search
    res = [x for x in seq1 if x in seq2]
    return res


s1 = 'school'
s2 = 'college'
r = intersect(s1, s2)
print(r) # ['c', 'o', 'o', 'l']

# polymorphism in action
r = intersect([1, 4, 6, 3], (3, 4)) # mixed types
print(r) # [4, 3]

# ============= Scopes / Namespaces ================ # 
x = 5
def func():
    x = 10
    print(x)

func() # prints 10
print(x) # still 5
# the x inside func() is inside func's namespace and the x outside (in the module) is in this module's namespace
# so even though both names are x, they are distinct. infact the x inside def is not even available outside the func() body. its garbage collected.

# anything that is assigned inside a def, will become local to that function. 
def func2():
    import os
    print(os.getcwd())

func2()
try:
    print(os.getcwd()) # raises NameError as os was never defined in the module namespace
except NameError:
    print('os module was never available outside the func2. because the name `os` exists inside func2 only.')
    print('therefore our try statement failed and we are in the except clause.') # above try failed and so this statement, i.e. the except part runs


def func3():
    importt sys


