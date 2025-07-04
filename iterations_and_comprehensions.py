# we say in looping_constructs.py that for loops can be used on any sequence type - lists, tuples and strings
for x in 'spam': print(x * 2, end= ' ')

print()
# actually the for loop turns out to be even more generic - it works on any *iterable object*

f = open('file_objects_io/file1.txt')
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line) # length 0, empty string, implies end of file (EOF)
line = f.readline()
print(len(line), line) # length 0, empty string

# instead of f.readline() we could use next() as file object is an iterable
f = open('file_objects_io/file1.txt')
while True:
    try:
        print(f.__next__())
    except StopIteration as e:
        print('StopIteration Error at end of file')
        break
print() # blank line for clarity of output

# infact you dont need to code all of this as python's for loop handles this for us and catches the StopIteration
print('Reading a file line by line - ideal way')
for line in open('file_objects_io/file1.txt'):
    print(line.upper(), end='')

# the below while loop is an alternative to the above for loop for reading files line by line
f = open('file_objects_io/file1.txt')
while True:
    line = f.readline()
    if not line: break # at EOF we get empty string and empty string is False in python
    print(line, end='')

print()
# iter and next()
print("Using obj.__next__() and next() for manual iteration")

f = open('file_objects_io/file1.txt')
print(next(f))
print(next(f))

f = open('file_objects_io/file1.txt')
print(f.__next__()) # same as above next(f)
print(f.__next__())

# technically, when a for loop starts, it passes the sequence or iterable to the iter() built-in and then
# uses its returned result to iterate using next()
L = [1, 5, 9]
I = iter(L)
print(I is L) # False
print(I.__next__()) # 1, doing L.__next__() raises AttributeError
print(next(I)) # 5 # next(I) is same as I.__next__()
print(I.__next__()) # 9, the subsequent call to next will raise StopIteration error as there are no more items to fetch

# for files we dont need to pass them to iter() because they already have the __next__() method
f = open('file_objects_io/file1.txt')
print(f.__next__())
I = iter(f)
print(I.__next__())
print(I is f) # True

# when iterating manually use try except to catch the StopIteration error
L = [1, 5, 9]
print(L)
I = iter(L)
while True:
    try:
        x = I.__next__()
    except StopIteration:
        break
    print(x ** 2, end = ' ')

print()

# iterating a dictionary
# the classic way is to loop through the dictionary keys
D = {'a': 5, 'g': 88, 's': 100}
print(D)
for key in D.keys():
    print(key, D[key])

# in recent versions of python though, dictionaries have an iterator that returns 1 key at a time in an iteration context
I = iter(D)
print(next(I))
print(I.__next__())
print(next(I))

# therefore we dont even need to do D.keys() when iterating because the for loop uses the iteration protocol
# to grab one key at a time
for key in D:
    print(key, D[key])

import os
P = os.popen('dir')
print(P.__next__())
print(P.__next__()) # but next(P) is not supported and raises TypeError. this is only an implementation issue.
# but for loops iterate through these objects just fine.
P = os.popen('dir')
for item in P:
    print(item, end='')

# range() is an iterable in python
r = range(2, 8)
print(r)
print(type(r))
I = iter(r) # r does not have __next__() method
print(next(I))
print(next(I))
print(I.__next__())
print(list(I)) # creates a list, but only of the remaining elements
print(list(r)) # to collect all results at once

# enumerate() is an iterable
e = enumerate('spam')
print(e)
print(type(e))
print(e.__next__()) # so enumerate is an iterator too. you dont really need to pass it to iter()
I = iter(e) # only the remaining elements
print('Iterating through I')
print(I.__next__())
print(next(I))

