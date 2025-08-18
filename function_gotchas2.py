# default arguments and mutable objects
def saver(x=[]):
    x.append(1)
    print(x)

saver([2, 3]) # prints x as [2, 3, 1]

saver([4, 5]) # [4, 5, 1]

saver() # uses the default value []. prints [1]
saver() # uses the default value/object x references which is now not [] but [1]. therefore prints [1, 1]

saver() # prints [1, 1, 1]
# NOTE that x is not available in the global scope. so while a mutable object helps in keeping state information between function calls, it is not available outside the function

# if this is not the behaviour you want, simply make a copy of the default argument in the function body so that on each function call you are working on a copy and therefore different function calls
# do not affect that default argument anymore. or do it like below
def saver(x=None):
    if x is None: # no argument passed
        x = [] # make a new list
    x.append(1)
    print(x)

saver([3, 2]) # prints [3, 2, 1]
saver() # [1]
saver() # [1]
saver() # [1]

a = [4, 5]
saver(a) # prints [4, 5, 1]
print(a) # a is updated to [4, 5, 1]

a = []
saver(a) # prints [1].
print(a) # [1]

# as a side note, if you replaced the if test with a truth test or condition based
def saver(x=None):
    x = x or []
    x.append(1)
    print(x)

saver([2,3]) # [2, 3, 1]
saver() # [1]
saver() # [1]

a = []
saver() # prints [1]
print(a) # a is still [], i..e empty list because the or truth test in the function body returned the right side [] which is not referenced by a. its a different objectt

x = []
y = []
print(x is y) # False. both are different objects in different memory locations

x = None
y = None
print(x is y) # True


# using function attributes to achieve the same thing as mutable defaults can be less confusing
def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver() # [1]
saver() # [1, 1]
saver() # [1, 1, 1]
print(saver.x) # [1, 1, 1]


# function gotcha - 3 -- functions without returns
# technically, functions without a return or yield statement, return None
def proc(x):
    print(x)

x = proc('spam') # prints spam
print(x) # None

l = [4, 5, 6]
l = l.append(55)
print(l) # None. l is assigned None now because .append() does not return anything (so returns None) and you have lost your original list in doing so.
# recall that append makes changes in-place

