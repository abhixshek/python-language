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

