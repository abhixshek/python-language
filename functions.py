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
# global x # this statement will give error.
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
print(x, v) # [6, 7], 'spam'

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

# minimize cross-file changes:
# although we can change variables in another file directly, we usually should not.
x = 50
print(x)
import functions2
print(functions2.x) # here we are referencing, which is okay and absolutely normal practice.
# prints 100
functions2.x = 78 # such changing of imported module variables can be subtle and implicit leading to inflexible code, bugs, and maintenance nightmare.
print(functions2.x) # 78

# a more explicit way to do would be to have an accessor function defined in the function2 module that allows to change x.
x = 50
print(x)
from imp import reload
reload(functions2)
print(functions2.x) # 100
functions2.setX(34)
print(functions2.x) # 34

# other ways to access globals (see functions3.py as reference for below code)
import functions3
print(functions3.var) # 98
functions3.test()
print(functions3.var) # 102
"""Go through functions3.py and functions4.py to understand some nuances """

# nested functions and scopes
x = 99 # global scope name

def f1():
    x = 88 # enclosing def local
    def f2():
        print(x) # reference made in nested def
    f2()

f1() # prints 88: enclosing def local
print(x) # 99, global scope was never referenced in either f1 or f2

# NOTE that this is all legal python code. because function definition in python is nothing but a statement, it can appear anywhere where any other statement can. 
# f2() # you cannot call f2 in the module scope/global scope because its a name not known to the module scope. It is a local name in f1 just like
# any other variable created in f1

# NOTE in a sense, f2 is a temporary function that lives only during the execution of (and is visible only to code in) the enclosing f1.

# this LEGB rule works even if the enclosing function has already returned.

x = 99
print(x)
def f1():
    x = 77
    def f2():
        print(x) # remembers x in encloding def scope
    return f2 # return f2 but dont call it

action = f1() # make, return function
# now action is nothing but another name for the function f2
action() # prints 77
print(x) # 99, x in the global scope was unchanged

# these nested functions that are returned by the enclosing function are called factory functions. because they can remember state of the enclosing function it allows
# for adjusting the behaviour of the returned function based on the outer function's variable values (ex: user input received)
def maker(N):
    def action(X): # make and return action
        return X ** N # action retains N from enclosing scope
    return action

f = maker(2) # so N=2
print(f) # f is a function object
print(f(3)) # X=3, 3 ** 2
print(f(4)) # x=4, 4 ** 2

g = maker(3) # N=3
print(g(3)) # 3 cubed, 3 ** 3
print(g(4)) # 4 cubed, 4 ** 3
print(f(5)) # 5 squared. f still remembers the N value it was created on.

# using default arguments for retaining state information
def f1():
    x = 88
    def f2(x=x):
        print(x)
    f2()

f1() # prints 88. the function f2's header is run before python steps into f2, which means that in x=x, the right side x is still referring to the x in f1 because the program
# is still in f1's scope. once program execution enters inside f2, the default argument has already been captured.

# the best thing to do for most code is to avoid using nested defs.
# the above can be achieved alternatively as below:
def f1():
    x = 82 # pass x along instead of nesting
    f2(x) # forward reference is okay. as long as f1 is called only after f2 has been defined.

def f2(x):
    print(x)

f1() # f1 function definition has f2 function call. therefore you can call f1, only after f2 has been defined. otherwise you will get a NameError
# prints 82


# nested scopes and lambdas
# it should be clear by now but just to repeat, lambda is an expression, not a statement
# its an expression that generates a new function to be called later, much like a def statement.
# because it is an expression, it can be used in places that def cannot, for example within lists and dictionary literals.

def func():
    x = 4
    action = (lambda n: x ** n) # x remembered from enclosing scope
    return action

x = func()
print(x(2)) # 4 ** 2 = 16
print(x(3)) # 4 ** 3 = 64

# before the introduction of enclosing scopes in python, default arguments was the way to achieve the above
def func():
    x = 4
    action = (lambda n, x=x: x ** n) # pass x in manually
    return action

x = func()
print(x)
print(x(2)) # 16
print(x(3)) # 64


# an exception to the enclosing scope rule is when nested functions are created inside a loop that is in the enclosing function
# all functions generated within the loop will have the same value - the value the referenced variable had in the last loop iteration.
def makeActions():
    acts = []
    for i in range(5): # tries to remember each i
        acts.append(lambda x: i ** x) # all remember same last i!!
    return acts

acts = makeActions()
print(acts[0])
# the above does not quite work the way we actually wanted because the enclosing scope variable is looked up when the nested functions are later called
# and this means they all remember the last iteration value)
print(acts[0](2)) # 16, but should have been 0 ** 2 = 0
print(acts[1](2)) # 16, but should have been 1 ** 2 = 1
print(acts[2](2)) # 16, but should have been 2 ** 2 = 4
# i.e. we get back 4 ** 2 for all of the functions returned

# this is one case where we still have to rely on default arguments to achieve what we want to achieve.
# BECAUSE defaults are evaluated when the nested function is created (not when its later called)
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x) # remmeber current i
    return acts

acts = makeActions()
print(acts[0](2)) # 0 ** 2 = 0
print(acts[1](2)) # 1 ** 2 = 1
print(acts[2](2)) # 2 ** 2 = 4

# this is fairly obscure case of nested functions, but it can come up in practice, especially in code that generates callback handler functions for a number of widgets in a GUI
# (eg: button press handlers).

# arbitrary scope nesting
def f1():
    x = 99
    def f2():
        def f3():
            print(x) # found in f1's local scope
        f3()
    f2()

f1() # prints 99


# nonlocal statement
def tester(start):
    state = start
    def nested(label):
        print(label, state) #remembers state in enclosing scope
    return nested

f = tester(0)
f('spam')
f('ham')
f1 = tester('boy')
f1('school')
f1('college')

def tester(start):
    state = start
    def nested(label):
        print(label, state)
        state += 1 # cannot change enclosing scope names
    return nested

f = tester(5)
# f('spam') # running this expression raises error. UnboundLocalError: local variable 'state' referenced before assignment
# think from python's view. updating the state value above is ambigious. are you trying to create a local variable state which is equal to state (of outer def) + 1
# or are you updating the value of state created in the outer def (enclosing def scope).
# this is ambigous and python does not like ambiguity and hence the error.

# nonlocal declaration makes the assignment explicit
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1 # allowed to change it if nonlocal
    return nested

f = tester(4)
f('spam') # increments state on each call
f('ham')
f('monty')

f1 = tester(35) # each returned function gets its own state. 
f1('spam')
f1('hello')
f('india') # increments state of tester for the function f we created above, not this tester state as stored in f1. 
# each nested function remembers its distinct state.

# a few boundary cases on nonlocals
"""
state = 10
def tester(start):
    def nested(label):
        nonlocal state
        print('this is a nested def.')
    return nested
"""

# the above snippet raises SyntaxError: no binding for nonlocal 'state' found EVEN BEFORE the below function call statements.
# because recall SyntaxErrors are found before runtime.
# f = tester(0)
# f()
# this is unlike global declaration statement which did not raise any error for any name that did not exist in the global scope
# ofcourse not that it was any useful, because just declaration statement does not achieve anything. and the moment you referenced that non-existing name in any other statement it would 
# throw a NameError
# nonlocal is even more stricter in that it needs the name to be present in the enclosing function when the nonlocal statement is encountered (in the function body)
# also note that having state = 10 in the module scope or global scope did not help as nonlocal restricts name search only to the enclosing defs. it does not care what names you have created
# in the global scope / module file.


def tester(start):
    if '5':
        a = 5
    else:
        b = 10
    def nested(label):
        nonlocal start, state
        print('this is a nested def.')
    state = 100
    return nested


# note that start was never referenced in any statement in the enclosing scope or the nested function body. although this is does not achieve anything material. but the point is no error
# was raised as long as the name used in nonlocal exists in the enclosing scope
f = tester(0)
f('spam') # prints this is a nested def. and works just fine.

def tester(start):
    if '5':
        a = 5
    else:
        b = 10
    def nested(label):
        nonlocal start, state
        print('this is a nested def. {0}'.format(state))
    state = 100
    return nested

f = tester(0)
f('spam')

def tester(start):
    def nested(label):
        global st
        st = 98 # this creates the name in the module scope
        print(label, st)
    return nested

f = tester(0)
f('spam') # st did not exist before this function call.
print(st) # 98

# in summary, NOTE Python must resolve nonlocals at function creation time, not function call time.

# state information with function attributes
def tester(start):
    def nested(label):
        print(label, nested.state) # nested is in enclosing scope
        nested.state += 1 # Change attr, not nested itself
    nested.state = start # Initial state after func defined
    return nested

F = tester(0)
F('spam')
F('ham')
print(F.state) # can access state outside functions too
F('school')

G = tester(42)
G('boy')
G('girl')
F('college') # G has its own state, does not overwrite F's state
print(F.state) # 4
print(G.state) # 44
print(F) # <function tester.<locals>.nested at 0x00000204DECCAB80>
print(G) # <function tester.<locals>.nested at 0x00000204DECCAC10> 


## below is some testing of the same concepts on mutable objects like lists.
def tester(inp1):
    a = inp1
    b = [4, 5, 6]
    def nested(label):
        print(label, inp1)
        inp1.append(56)
        b.append(33)
        # inp1 = 5 # this statement does not work. but the above append works. i.e. we are able to change mutable objects without using the nonlocal declaration.
        print(inp1)

    print(a)
    return nested

f = tester([3, 4])
f('spam')
f('ham')


### argument passing
def f(a): # a is assigned to (references) the passed object
    a = 99 # changes local variable a only

b = 88
f(b) # a and b both reference 88 initially
print(b) # b is NOT changed. still 88

def changer(a, b): # arguments assigned references to objects
    a = 2 # changes local name's value only
    b[0] = 'spam' # changes shared object in-place

X = 1
L = [3, 4] # caller (in this case module scope)
print(X, L)
changer(X, L) # pass immutable and mutable objects
print(X, L) # X is unchanged. L is different!

# the net effect of dealing with mutable function arguments is that they can act as both the input to your function and the output from your function.

# if we dont want the change to the passed in arguments in the caller, pass explicit copies instead.
X = 1
L = [3, 4]
print(X, L)
changer(X, L[:]) # L[:] is a copy of the list object that L referenced
print(X, L) # X is unchanged. L is also unchanged.

# or create copy inside the function
def changer(a, b):
    b = b[:] # copy input list, so we dont impact caller
    a = 2
    b[0] = 'spam' # changes our list copy only

X = 1
L = [3, 4]
print(X, L)
changer(X, L)
changer(X, L[:])
print(X, L) # X and L are unchanged in the caller (i.e. in the module scope)

# to really prevent changes, pass immutable objects to force the issue.
try:
    changer(X, tuple(L))
except TypeError:
    print('Ran into TypeError because you attempted to change an immutable object in the function')

# updating passed in argument names and assigning the results back to them
def multiple(a, b):
    a = 2
    b = [3, 4]

    return a, b # returning the updated objects for each passed in argument

X = 1
L = [1, 2]
print(X, L)
X, L = multiple(X, L) # assign results to caller's names. tuple unpacking is at work here.
print(X, L)

"""
def f((a, (b, c))):
    print('hello')

f((1, ((6, 7)))
"""
# !!!!
# The above function header having a single tuple passed and then internally assigning the elements to a, b, and c
# using tuple unpacking is NO LONGER SUPPORTED in Python 3.0
# this also applies to similar tuple unpacking in lambda function argument lists
# !!!!
# you need to use explicit tuple unpacking in the function body to achieve the above
def f(T):
    (a, (b, c)) = T
    print(a, b, c)

f((1, (6, 7)))
f((3, [5, 9]))
f([6, [3, 2]])
# notice how different types of sequences are supported in the unpacking. refer to assignments.py file as this is all based on that same assignment model. nothing is new here. 


# special argument-matching modes:

# 1. the simple case of positional arguments
# function header defines 3 arguments/parameters, you pass 3 arguments in the function call
def f(a, b, c):
    print(a, b, c)

f(3, 'spam', 5) # a is matched to 3, b is matched to 'spam', c is matched to 5
f([6, 7], 'hello', 23)

# 2. passing values by keywords in the caller
f(a=3, b='new', c=100)
f(c=5, a=78, b=0) # you can change the order of arguments passed as they are going to be assigned by their names anyway
# prints 78 0 5

"""
>>>f(a=5, c = 3, b= 100, a= 10)
  File "<stdin>", line 1
SyntaxError: keyword argument repeated
"""


"""
>>>f(a=5, c = 3, d= 100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got an unexpected keyword argument 'd'
"""

# mixing positional and keyword arguments in the caller
f(10, c=67, b=33) # prints 10 33 67
# positional comes first then keywords and they can be in whichever order you like

"""
>>>f(a=10, 67, b=33)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
"""

# defaults
def f(a, b=1, c=5): print(a, b, c)


f(66, c=20, b=10) # prints 66 10 20
f(c=90, b=88, a=77) # prints 77 88 90

f(55) # this means a=55 because a is a required argument. and since you did not pass any other argument, b and c will take their defaults
# prints 55 1 5

f(a=90) # prints 90 1 5

f(33, 44) # a=33, b=44, c takes its default = 5. prints 33 44 5

f(5, 6, 7) # prints 5 6 7

f(77, c=23) # notice positionally a is matched with 77 and then we directly provided c keyword argument skipping b. but this works and b takes its default
# prints 77 1 23


def func(spam, eggs, toast=0, ham=0): # first 2 required
    print((spam, eggs, toast, ham)) # print a tuple

# as you can tell from the function header, you need to pass AT LEAST 2 arguments.
func(1, 2) # (1, 2, 0, 0)
func(1, ham=5, eggs=10) # (1, 10, 0, 5)
func(eggs=9, spam=22) # (22, 9, 0, 0)
func(toast=8, eggs=3, spam=2) # (2, 3, 8, 0)
func(5, 6, 3, 1) # all by position. (5, 6, 3, 1)


##  arbitrary arguments

# *name in the function header:- collects positional arguments into a tuple
def f(*args):
    print(args)
    print(type(args)) # tuple


f(5) # args = (5,)
f(7, 8, 9) # args=(7, 8, 9)
f([3, 4, 10]) # args=([3, 4, 10],) . NOTICE the entire list is 1 argument.

f() # args=() # an empty tuple

# **name in the function header:- collects keyword arguments into a dictionary
def f(**args):
    print(args)
    print(type(args)) # dict

f(a=5, b=23, c=90, d='spam')
# even though you have passed multiple keyword arguments they all became keys of a dictionary as key:value pairs. so you cannot directly reference a, b, c, etc in an expression
# in the function body. you have to use them as keys of the dictionary. they are not local variable names in your function.

f() # empty dictionary is assigned to args, i..e args={}
f(a=9)
f(e=[(4, 5), (7, 8)])

def f(a, b, c=5, *pargs, **kargs):
    print(a, b, c)
    print(pargs)
    print(kargs)

f(5, 10)
# a=5, b=10, c=5, pargs=(), kargs={}


"""
f(3)
TypeError: f() missing 1 required positional argument: 'b'
"""

f(3, 4, 23)
# a=3, b=4, c=23, pargs=(), kargs={}

"""
f(4, 5, 6, 7, c=22)
TypeError: f() got multiple values for argument 'c'
"""

f(4, 5, 6, 7, t=100)
# a=4, b=5, c=6, pargs=(7,), kargs={'t': 100}

# unpacking arguments - in the function call
# in the function call, using * syntax unpacks a collection of arguments

def f(a, b, c, d): print(a, b, c, d)

f(*(4, 5, 'spam', 3.14))

# similarly, the ** syntax unpacks a dictionary into individual keyword arguments
d = {'d': 5, 'b': 10, 'c': 'school', 'a': 100}
f(**d)

# you can combine all these techniques ina single function call
f(*(1, 4), **{'d': 55, 'c': 32})
# a = 1, b = 4, c = 32, d = 55

f(44, *[8, 9], **{'d': 56})
# a=44, b=8, c=9, d=56

f(44, *'sp', **{'d': 56})
# a=44, b='s', c='p', d=56

"""
f(44, *[8, 9, 10], **{'d': 56})
TypeError: f() got multiple values for argument 'd'
"""

f(5, c=7, *(3, ), **{'d': 10})
# a=5, b=3, c=7, d=10

f(3, c=7, *(5,), d=99)
# a=3, b=5, c=7, d=99

f(1, *(2,), c=3, **{'d':4})
# a=1, b=2, c=3, d=4

# the * syntax in the function call accepts any iterable, not just sequences.
file = open("file_objects_io/file1.txt")
def func(a, *args):
    print(a)
    print(args)

func(*file) # 1st line of the file is assigned to a, and the rest of the lines are part of the tuple `args`


# this */** syntax  (varargs) is useful when you want/need to build up the function arguments at runtime and that are arbitrarily many. 

def tracer(func, *pargs, **kargs): # accept arbitrary arguments
    print("calling:", func.__name__)
    return func(*pargs, **kargs) # pass along arbitrary arguments

def add(a, b, c, d):
    return a + b + c + d

result = tracer(add, 1, 2, c=5, d=10)
print(result) # 18

# keyword-only arguments
# arguments that appear after *args in the argument list in the function header are treated as keyword-only args
# all such arguments must be passed as keyword args in the function call
def kwonly(a, *b, c):
    print(a, b, c)

"""
>>>kwonly(1, 2, 3, 4)
TypeError: kwonly() missing 1 required keyword-only argument: 'c'
"""

kwonly(1, 2, 3, c=4)
# a=1, b=(2, 3), c=4

kwonly(1, c=10)
# a=1, b=(), c=10

kwonly(c=7, a=4)
# a=4, c=7, b=()

kwonly(5, 6, c=7)
# a=5, b=(6,), c=7

def func(a, *, b, c): # NOTICE just the * in the function header. this is a special syntax that tells python that this function accepts no variable-length arguments list
    print(a, b, c)
# a can be passed as a positional or a keyword argument, but b and c must be passed as keyword args only.
# and no other extra positional arguments can be passed

"""
>>>func(1, 2, 3)
TypeError: func() takes 1 positional argument but 3 were given
"""

func(1, c=4, b=2)
# a=1, b=2, c=4

func(c=10, b=3, a=88)
# a=88, b=3, c=10

d = dict(c=10, b=5, a=1)
print(d)
func(**d)
# a=1, b=5, c=10

"""
>>> func(1)
TypeError: func() missing 2 required keyword-only arguments: 'b' and 'c'
"""

def func(a, b=3, *, c, d=10): # c and d when passed MUST be passed as keyword arguments. because d has a default, it is optional when passing. but when passed it must be passed as a kw argument.
# b has a default value. therefore it is optional. when passed it can be passed as positional or keyword argument, as it appears before the * in the header.
    print(a, b, c, d)

func(1, 2, c=4, d=15)
# a=1, b=2, c=4, d=15

func(d=5, a= 6, c= 14, b=90)
# a=6, b=90, c=14, d=5

func(1, b=5, c=8)
# a=1, b=5, c=8, d=10

func(1, c=44) # c is a required kw argument.
# a=1, b=3, c=44, d=10

"""
def func(a=5, b, c, d):
    print(a, b, c, d)

# this function definition gives a Syntax error because a non-default argument follows a default argument
# but NOTICE that the previous func definition had def func(a, b=3, *, c, d=10) and it worked because c is a keyword only argument so even if a default arg appears before it
# it does not cause any ambiguity.
"""

def func(a, b=5, *, c=3, d, e=9):
    print(a, b, c, d, e)

# a must be passed as positional/keyword
# b can be optionally passed as positional/keyword. if not passed it takes the default value
# no extra positional arguments can be passed as we have used * only, and not *name
# c, d, and e are all keyword-only arguments.
# c and e are optional but d must be passed.
func(66, d=10)
# a=66, b=5, c=3, d=10, e=9

func(d=8, a=77)
# a=77, b=5, c=3, d=8, e=9

func(d=8, a=77, b=2, c=2)
# a=77, b=2, c=2, d=8, e=9

func(40, 70, d=90)
# a=40, b=70, c=3, d=90, e=9

# NOTE kw-only args must appear after the * or *name argument and they CANNOT appear after **kargs argument. Also note that there is no `**` without a name syntax for arbitrary keyword arguments.
"""
>>>def kwonly(a, **pargs, b, c):
SyntaxError: invalid syntax

>>>def kwonly(a, **, b, c):
SyntaxError: invalid syntax
"""

def func(a, *b, c=4, **d): # c is a kw-only arg
    print(a, b, c, d)
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

func(2, 6, 8, 3, 2, c=10, d=100, e=45, f=34) # do not get confused with d here in the function call and the d in the header. they are not the same and in-fact in the function header d is a dictionary
# that will have one of the keys 'd' because you passed it in the function call.

func(2, 6, 8, 3, 2, r='spam', t='school') # c took the default value of 4. c is a kw-only argument. if you are passing, then must pass it as a keyword argument. if not passing, it will take the default
# because a default is defined in the function header. had a default not been defined, it would have been MUST for you to pass c in the function call as a keyword argument.

func(1, 2, 3, 4, q=10, w=5, c=99)

def func(a, c=6, *b, **d): # c is NOT a kw-only arg here
    print(a, b, c, d)

func(2, 3, 4, 5, x=70, y=90)
# c=3

func(4, 8, 9)
# a=4, b=(9,), c=8, d={}
func(33, p=80)
# a=33, c=6, b=(), d={'p': 80}


# NOTE During function calls, i.e., when keyword-only arguments are passed, they can appear before or after **args form. The kw-only argument can be coded either
# before or after the *args, and may be included in **args.

def f(a, *b, c=6, **d): # c is a kw-only arg
    print(a, b, c, d)

f(1, *(2, 3), **dict(x=4, y=5)) # c takes the default value of 6

f(1, *(2, 3), **dict(x=4, y=5), c=7) # c=7

f(*(1, 2, 3), **dict(x=4, y=5), c=8) # c=8

f(c=7, *(1, 2, 3), t=9, **dict(x=4, y=5)) # c=7
# prints 1 (2, 3) 7 {'t': 9, 'x': 4, 'y': 5}

f(c=7, *(1,), **dict(x=4, y=5)) # NOTICE you can pass kw-only args before *args in the call but cannot pass kw-only args before standalone positional arguments.
# that will give you Syntax error saying positional argument follows keyword argument.

f(c=7, a=90, u=2, i=45)

f(8, 9, 10, **dict(c=15, d=88, e=66))

f(8, 9, 10, **dict(d=88, e=66), c=76)

# suppose you want to code a function that is able to compute the minimum value from an arbitrary set of arguments and an arbitrary set of object data types.
# the function should work for all kinds of Python object types: numbers, strings, lists, lists of dictionaries, files, and even None.

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest): # in this definition we can avoid the indexing to separate the first element and the rest that we had to do in min1()
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1(3, 4, 2, 9, 1, 5, 6))
print(min2(3, 4, 2, 9, 1, 5, 6))
print(min3(3, 4, 2, 9, 1, 5, 6))
# all 3 return the same answer = 1

print(min1("bb", "aa"))
print(min2("bb", "aa"))
print(min3("bb", "aa"))
# answer = "aa"

print(min1([3, 4], [3, 2, 1], [3]))
print(min2([3, 4], [3, 2, 1], [3]))
print(min3([3, 4], [3, 2, 1], [3]))
# answer = [3]

print(min1(True, False))

# NOTE that we are not checking for the case when no arguments are passed in either of the 3 function definitions. Because our functions accept all kinds of arguments, there is no
# sentinel value that we could pass back to designate an error.
# we let python take care of raising an error and this is exactly what we want.

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def greaterthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 6, 5))
print(minmax(greaterthan, 4, 2, 1, 6, 5))

# python provides min and max built-in functions that are implemented in c for speed.
print(min([3, 1, 2])) # 1 argument, a list is passed.
print(min(3, 1, 2)) # multiple arguments passed


# generalized set functions (intersect and union) using varargs concept
def intersect(*args):
    res = []
    for x in args[0]: # Scan first sequence
        for seq in args[1:]: # For all other args
            if x not in seq: # Item in each one?
                break # No: break out of loop
        else:
            res.append(x) # Yes: add items to end
    return res

print(intersect([3, 4, 5], [1, 9, 0, 4], (1, 2, 4))) # mixed types

def union(*args):
    res = []
    for seq in args: # for all args
        for item in seq:  # for all items
            if item not in res:
                res.append(item) # add new items to result
    return res

print(union([3, 4, 5], [1, 9, 0, 4], (1, 2, 4)))

s1, s2, s3 = "SPAM", "SCAM", "SLAM"
print(intersect(s1, s2, s3))
print(union(s1, s2, s3))

# NOTE that python provides the set object type, which means you dont need to code such functions to perform mathematical intersection or union operations. just use set built-ins.

