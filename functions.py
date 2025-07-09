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


import builtins # contains everything in the built-in scope/namespace. 
print(builtins is __builtins__)
print(dir(builtins)) # notice open(), len(), True, False, list(), zip(), the built-in exceptions, etc.
# you find in the list names None, True and False as well. though they are treated as reserved words.

# so you can either directly use the built in names in your program or import builtins then use that name
print(len([3, 4]))
# or do
print(builtins.len([3, 5]))

# python has LEGB rule, which is search local first then enclosing then global then builtins
# which means builtin names can be overidden. 
def func():
    open = "spam"
    # f = open('file_objects_io/file1.txt') # this will not run now as open refers to str object now. therefore having this open() statement raises SyntaxError on function call.
    print(open)
    print(type(open))


func()
f = open('file_objects_io/file1.txt') # outside the function we are back to the builtin scope's open. and that open initialized inside the above function is not available here.
# infact if I assign open to something here in the module namespace then I permanently loose the open() file constructor in the rest of my program.
print(f.readline())


# global statement
x = 10
# global statement cannot be typed at the module level, i.e in the top level of the module file. It will result in syntaxError.
print(x)

def func():
    global x
    global v
    print(x)
    x = 40 # global x gets changed


func()
print(x) # x in the module level which was previously 10 is now having value 40
# NOTE that in the above function definition we have global v statement and even though v name does not exist yet in the program, the func call did not raise any NameError.
# but doing this does not achieve anything because when you use v in any expression, you will then get a NameError.
x = 15
v = 30
print(x, v)
def func():
    global x, v # declaring multiple names as global
    print(x, v)
    x, v = [6, 7], 'spam'
    print(x, v)
func()
print(x, v)

y, z = 1, 2
print(y, z)
def func():
    global x
    x = y + z

func()
# NOTE that x, y, z are all global. y and z are global because they are not assigned in the function. also note that y and z were never assigned inside the function def
# but python's LEGB rule find them in the module automatically.
# had x not been declared global in the def it would have been a local variable to the function and not accessible outside the function.
print(y, z)
print(x) # x which was assigned inside def is even available outside, i.e, in the module scope even though it did not even exist before the function call. the assignment statment inside def created it
# in the module namespace (because of global declaration)
# prints 3


# minimize and avoid using global in your programs as it leads to difficulty in debugging as different functions at different times during the execution of your program may be changing the global variabl's
# value, it becomes difficult to track.
x = 99
def func1():
    global x
    x = 88

def func2():
    global x
    x = 77
# Now, imagine that it is your job to modify or reuse this module file. What will the value of X be here? Really, that question has no meaning unless it’s qualified with a point of
# reference in time—the value of X is timing-dependent, as it depends on which function was called last (something we can’t tell from this file alone).


