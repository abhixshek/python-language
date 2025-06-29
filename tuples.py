a = () # empty tuple
print(a)
print(type(a))
print(len(a))

a = (4, ) # 1 item tuple
print(a)
print(len(a))
a = (4) # integer expression, not a tuple. to create a tuple 1 comma is needed like in the above example
print(a)
print(type(a))

a = (1, 2)
b = (5, 6)
result = a + b # concatenation
print(result)
print(a)
print(b)

r = a * 4 # repetition
print(r)
print(len(r))

a = (6, 7, 9, 2, 4, 2, 4, 3, 1)
print(a)
print(a[2]) # indexing
print(a[2:5]) # slicing

# parenthesis are not always needed for tuples
a = 5, 7, 3, 2
print(a)
print(type(a)) # a tuple

# since tuples are immutable they dont support sorting
# to sort a tuple covert it into a list, sort the list, and convert back to a tuple
T = ('cc', 'DD', 'aa', 'bb')
print(T)
tmp = list(T)
tmp.sort()
print(tmp)
T = tuple(tmp)
print(T) # sorted tuple

# or use the sorted() built-in which returns a list no matter what the iterable passed is.
T = ('cc', 'DD', 'aa', 'bb')
t = sorted(T)
print(t)
T = tuple(t)
print(T) # sorted tuple

a = (5, 7, 2, 4, 1)
print(a) # a tuple
result = [x + 10 for x in a]
print(result) # result is a list

a = (5, 7, 2, 4, 7, 9, 4, 2, 1, 2, 3, 5)
print(a)
c = a.count(2) # count the no of occurences of 2
print(c)

r = a.index(2) # return the offset of the first occurence of 2
print(r)
r = a.index(2, 8) # return the offset of the first occurence of 2 starting from the index 8
print(r) # 9 in this case
print(a[r])

# mutable object inside a tuple can still be changed. only the top level of the tuple is immutable.
a = ('spam', 98, [2, 5], 23.67)
print(a)
a[2][1] = 100 # cannot do a[2] = some object. will get TypeError 
print(a)


# None object
a = None
print(a)
print(type(a))
print(not a) # not a becomes True
# to allocate a 100 item list for later use if list's contents are not yet known to you
a = [None] * 100
print(a)
print(len(a))

# python provides a bool() built-in to test for boolean value of an object
print(bool(1)) # True
print(bool([5, 6])) # True
print(bool({})) # False

# type objects
x = [4, 5, 6]
t = type(x) # class list
print(t)
print(type(t)) # class type
print(type([1]) == type([]))
print(type([1]) == list)
print(isinstance([1], list))

import types # types contains other type names as well
def f(): pass
print(type(f) == types.FunctionType) # True

# repetition important points
l = [4, 5, 6]
print(l)
e = l * 4 # same as [4, 5, 6] + [4, 5, 6] + ...
print(e)
l[1] = 33
print(l)
print(e) # e is unchanged

l = [4, 5, 6]
r = [l] * 4 # same as [l] + [l] + [l] + ...
print(r)
l[1] = 67
print(l)
print(r) # r changed
# the thing to remember here is that repetition, concatenation and slicing copy only the top level of their operand
# objects



