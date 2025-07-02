# while loop is the most general looping construct
x= 'spam'
while x: # this same as the more verbose expression while x!= ''
    print(x, end=' ')
    x = x[1:]

print()
a, b = 0, 10
while a < b: # one way to code counter loops, we will see how to do this using for loops soon
    print(a, end=' ') # prints a from 0 upto, but not including b
    a += 1

print()
# NOTE that python does not have a 'do while' loop

# pass keyword
a = 5
while a > 0:
    pass  # do nothing.
    a -= 1

a = 5
while a > 0:
    ... # alternative to pass keyword. this is called ellipses
    a -= 1

def func1(): ... # can occur on the same line as header too.
print(func1()) # None as by default functions return None

X = ...
print(X) # Ellipses
print(type(X)) # <class ellipses>

# continue - skips to the top of the loop
x = 10
while x > 0:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=" ") # prints 8 6 4 2 0

print()
# continue should be used rarely as it reduces readability and maintainability
# alternatively we can achieve the above using if tests alone
x = 10
while x > 0:
    x = x - 1
    if x % 2 == 0:
        print(x, end=" ") # prints 8 6 4 2 0

print()

# break - terminate the enclosing loop
x = 9
while x > 0:
    x -= 1
    if x % 3 == 0: break
    print(x, end=" ") # prints 8 7

print()

# loop else. the else clause of loops is executed when no break statement is encountered. Also when the while loop never starts because the condition never evaluated to True to begin with, even then
# else clause is run.

def is_prime(x):
    if x == 1:
        print('1 is neither prime or a composite number.')
        return None # need to do this because otherwise the else clause of the while loop will run for x=1 even though the while loop test condition was never true, the else part runs because break statement
    # was not encountered.

    y = x // 2 # floor division by 2
    while y > 1:
        if x % y == 0:
            print('%i is not a prime number.' %x)
            break
        y -= 1
    else:
        print('%i is a prime number.' %x)

is_prime(1)
is_prime(2)
is_prime(3)
is_prime(10)
is_prime(19)


# for loops
for x in ['spam', 'ham', 'eggs']:
    print(x, end=' ')

print()

sum = 0
for x in [4, 5, 8, 2]:
    sum = sum + x

print(sum) # 19

prod = 1
for item in [4, 5, 2, 3]: prod *= item

print(prod) # 120

# iterate over a string
for x in 'school': print(x, end= " ")
print()

# iterate over a tuple (or any sequence really)
for x in (4, 7, 2): print(x, end=' ')
print()

# infact to iterate, any iterable works and therefore files and dictionaries work too

# tuple assignments to the target variable
T = [(4,3), (6, 7), (9, 0)]
for (a, b) in T: # tuple unpacking and assignment at work
    print(a, b)

# this type of tuple assignment is also seen when traversing 2 parallel sequences using zip(). see below
# this same pattern can be used on dictionaries to get key, value pairs from the .items() method
d = {'a': 44, 'b': 32}
for (key, value) in d.items():
    print(key, '=>', value)

# NOTE that tuple unpacking in the for loop header is just sequence assignment at work that we studied in assignments.py 
# this has nothing special to do with for loops. 
((a, b), c) = [(7, 8), 3]
print(a, b, c) # a=7, b=8, c=3

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)
# notice in the above that a string inside a list is a nested sequence because recall strings are sequences

# extended sequence unpacking
(a, *b, c) = (4, 5, 6, 7)
print(a, b, c) # a=4, c=7, b = [5, 6]
(a, *b, c) = 'school'
print(a, b, c) # a='s', c='l', b = ['c', 'h', 'o', 'o']

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)


for i in []:
    print('inside')
else:
    print('outside')
# in the above for loop, notice the empty list object. that means the loop body never ran. but the else clause of the loop ran because a break was never encountered and therefore outside is printed


# nested for loops
items = ["aaa", 111, (4, 5), 2.01] # A set of objects
tests = [(4, 5), 3.14] # Keys to search for
# test for existence of the key in tests in the items list
for key in tests: # For all keys
    for item in items: # For all items
        if key == item: # check for match
            print(key, 'was found')
            break
    else: # this else is associated with the inner loop, not the outer loop or the if statement
        print(key, 'not found!')
# because the nested if runs a break when a match is found, the loop else can assume that if it is reached, the search has failed.

# an easier and shorted code would be to use the `in` operator, although in implicitly scans an object(sequence) looking for a match
for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'not found!')

# NOTE this 2nd approach is preferred and in general you want to let python do as much of the work as possible for the sake of brevity and performance.

# find the common characters between the two strings
seq1 = 'spam'
seq2 = 'scam'

res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)

# range() iterator and loops
a = range(5)
print(a)
print(type(a))
print(list(a))
print(list(range(2, 10, 2))) # right bound is not included. and the last argument to range is the step size
print(list(range(5, -5, -1))) # goes in descending order from 5 to -4. -5 is not included

a = [3, 4, 7, 8, 4, 3]
for i in a:
    print(i, end=' ')
print()

# the above can be achieved using range and indexing
for idx in range(len(a)):
    print(a[idx], end=' ')
print()

# although the 1st approach, i.e. for i in a is preferred as python handles the details for you. 
# Don't use range calls in for loops except as a last resort
# but range allows us to do specialized traversals like skipping every other item
a = 'Programming'
print(a)
for i in range(0, len(a), 2): print(a[i], end=" ")
print()

# even for this, python offers a simpler appraoch, which is to use slices
print(a[::2])
for i in a[::2]: print(i, end=' ')
print()
# NOTE The only real advantage to using range here instead is that it does not copy the string and does not create a list in 3.0 (range is an iterator); for very large strings, it may save memory.

# another use case for range is when changing list items as you traverse.
a = [4, 7, 3, 2, 1]
print(a)
for item in a:
    item += 1
print(a) # a is unchanged because updating item does not change any object a is referring to

for i in range(len(a)):
    a[i] += 1
print(a) # updated

# using a while loop to achieve the same is possible, but requires more typing and maybe slower
i = 0
while i < len(a):
    a[i] += 1
    i += 1
print(a)

# but instead of the range and for loop combination we could also use list comprehension if we dont want to change the list in place
b = [item + 1 for item in a]
print(b)

# note that in the below loop, we are updating the list items in place without using range. this is possible because of the concept of references and list being a mutable object. and it has nothing to do 
# with for loop
a = [[4, 5], [6, 7]]
print(a)
for item in a:
    item.append(100)
print(a)

# using built-in zip() to traverse multiple sequences in parallel
# zip() is an iterator, to get all results at once use list() on top of it
a = [4, 5, 6]
b = [7, 8, 9]
print(a)
print(b)
z = zip(a, b)
print(z)
print(type(z))
r = list(z)
print(r)

for (x, y) in zip(a, b):
    print(x, y, '--', x+y)

# same can be achieved through manual indexing using a while loop but it would require more typing and be slower

# zip() accepts any iterable object or any sequence object as its arguments including files
# and it accepts more than 2 arguments
a = [1, 2, 3]
b = range(6, 9)
print(list(zip(a, b))) # [(1, 6), (2, 7), (3, 8)]

# NOTE zip truncates result tuples at the length of the shortest sequences when the argument lengths differ
s1 = 'abc'
s2 = 'school'
print(list(zip(s1, s2))) # [('a', 's'), ('b', 'c'), ('c', 'h')]

# map() built-in
s = 'spam'
result = list(map(ord, s)) # maps a function to each item of the iterable
print(result) # ASCII code of each character

# the above can also be achieved using list comprehension but map is generally faster.
result = [ord(c) for c in s]
print(result)

keys = ['a', 'k', 'g']
vals = [5, 7, 2]
# to create a dictionary from two sequences where one represents the keys and the other values
D = {}
for (k, v) in zip(keys,vals): D[k] = v
print(D)

# or use dict()
D2 = dict(zip(keys, vals))
print(D2)

# enumerate
# traditionally, to have both a counter and item while iterating in a loop, a separate offset/counter used to be created and then updated in the loop body
s = 'spam'
offset = 0
for c in s:
    print(c, 'appears at offset', offset)
    offset += 1

for (offset, c) in enumerate(s): # enumerate() returns a generator object
    print(c, 'appears at offset', offset)

e = enumerate(s)
print(e)
print(type(e))
print(next(e))
print(next(e))

