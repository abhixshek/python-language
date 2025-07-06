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

# list comprehensions
L = [5, 8, 3, 2, 9]
print(L)
for i in range(len(L)):
    L[i] += 10
print(L)

# the above works, but can be done faster using a list comprehension
L = [5, 8, 3, 2, 9]
L = [i + 10 for i in L]
print(L)

# in the context of files for example, when we read the lines, we get a `\n` at the end of each line except maybe the last line may or not have it.
# but we could iterate through the lines and remove the right side whitespace using line.rstrip() on each line and construct a new list.
f = open('file_objects_io/file1.txt')
lines = f.readlines()
print(lines)
lines = [line.rstrip() for line in lines]
print(lines)

# an even better approach is to not read all the lines first and let the iteration protocol take care of doing that as below
lines = [line.rstrip() for line in open('file_objects_io/file1.txt')]
print(lines)
# for large files, the speed advantage of list comprehensions can be significant compared to using a for loop

# you can chain multiple operations on a string object as each operation produces a new string
lines = [line.rstrip().split() for line in open('file_objects_io/file1.txt')]
print(lines)


lines = [('it' in line, line[0]) for line in open('file_objects_io/file1.txt')] # you can have any expression you want. here we are making tuples
print(lines)

# if clause within list comprehensions to filter out the results
lines = [line.rstrip() for line in open('file_objects_io/file1.txt') if line[0] == 'I']
print(lines)

# more complex form of list comprehension with nested iteration
res = [x + y for x in 'abc' for y in 'lmn']
print(res)
# its equivalent for loop statement is as shown below:
res = []
for x in 'abc':
    for y in 'lmn':
        res.append(x + y)
print(res)

# other iteration contexts
# the for loop, list comprehension, in membership tests, map(), sorted(), zip() all of these use the iteration protocol. i.e. anything that scans from left to right uses the iteration protocol.
r = 'Notice it even contains a backslash that is escaped (using double backslash) when read in python as a string\n' in open('file_objects_io/file1.txt')
# think of this expression as asking the question if "this line" in the file. i.e. in operator is not checking for words or characters here but entire line

print(r) # True
# NOTICE we did not even have to read the entire file contents at once to use the in operator

m = map(str.upper, open('file_objects_io/file1.txt'))
print(m)
print(type(m))
print(list(m))
# map is similar to a list comprehension but is more limited because it requires a function instead of an arbitrary expression.
# It also returns an iterable object itself in Python 3.0, so we must wrap it in a list call to force it to give us all its values at once.
m = map(str.upper, open('file_objects_io/file1.txt'))
print(m.__next__()) # prints the 1st line in uppercase
print(next(m)) # prints the 2nd line in uppercase

r = sorted(open('file_objects_io/file1.txt')) # sorted() returns a list object and not an iterable unlike map().
# but sorted() takes as input any iterable, not just list
print(r)

D = {'s': 4, 'y': 34, 'a': 100}
print(D)
print(sorted(D)) # returns a list of sorted keys

# other built ins that use the iteration protocol include sum(), min(), max(), any(), all(). note that all of these listed here return a single value/result
r = sum(range(5)) # sum() works on numbers only.
print(r)
a = [5,8,3,7,8,2]
print(min(a))
print(max(a))

r = any(['spam', [], (), {}, ''])
print(r) # True
r = all(['spam', [], (), {}, ''])
print(r) # False

# list() and tuple() also use the iteration protocol
r = list(open('file_objects_io/file1.txt'))
print(r)
r = tuple(open('file_objects_io/file1.txt'))
print(r)
r = '&&'.join(open('file_objects_io/file1.txt'))
print(r)

a, b, *c = open('file_objects_io/file1.txt') # sequence assignment uses iteration protocol too
print(a)
print(b)
print(c)

# dict(), set(), set and dict comprehensions all use iteration protocol
r = {ix: line for (ix, line) in enumerate(open('file_objects_io/file1.txt')) if line[0] == 'I'}
print(r)
