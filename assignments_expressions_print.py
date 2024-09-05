a = 'boy' # the most common
a, b = 'spam', 'ham' # this is called tuple-unpacking assignment. this is same as (a, b) = 'spam', 'ham'
# or (a, b) = ('spam', 'ham')
print(a)
print(b)

[c, d] = ['cool', 50.67] # same as above. called list-unpacking assignment. 
print(c) # cool
print(d) # 50.67

c, d = ['cool', 50.67] # works too

a, b, c, d=  'spam'
# assigns 's' to a. 'p' to b, etc. 

[a, b, c, d] = 'spam'
# works same as above.
# therefore bottom line is you can mix different different sequence object types of either side of the = sign. 
print(a, b, c, d)

w = 'cat'
a, b, c = w  # a='c', b='a', c = 't'

a, *b = 'spam'
print(a, type(a)) # assigns the 1st element to a
print(b, type(b)) # assigns rest of the sequence to b. b = ['p', 'a', 'm']
# when assigned this way, b will always be a list.

import numpy as np
np.random.seed(42)
arr = np.random.randint(50, size=(10, 1))
print(arr)
a, b, *c = arr
print(a) # a = arr[0] and since arr is a 2d array arr[0] is also a numpy array(vector)
print(type(a))

print(b) # b = arr[1]
print(c)
print(type(c)) # list of elements of arr from index 2. i.e. [arr[2], arr[3], arr[4], ...arr[9]]


np.random.seed(42)
arr = np.random.randint(50, size=(10,))
print(arr)
a, b, *c = arr
print(a) # int
print(b) # int
print(c) # list of integers because arr[2], arr[3], etc are all integers this time.

a = b = 'lunch'
# both a and b are assigned references to the same object 'lunch'
print(a, b)
# this is same as:
# b = 'lunch'
# a = b

# augmented assignment
r = 5
r += 10 # same as r = r + 10

# coding trick in python to swap variables using tuple assignment
a = 1
b = 2
b, a = a, b
print(a, b) # a is now 2 and b is now 1 without having to create a temporary third variable to be able to swap. 
# actually python stores the tuple on the right as a temporary object which allows us to achieve this swap. 


# advanced unpacking
s = 'SPAM' # a sequence of 4 characters
print(s)
# `a, b, c = s` # WILL NOT WORK as no. of items being unpacked and the no. of names on the left should be equal. 
a, b, *c = s
print(a)
print(b)
print(c) # c = list of remaining items of the sequence. therefore c = ['A', 'M'] i.e list('AM')

a, b, c = s[0], s[1], s[2:]
print(a)
print(b)
print(c) # c this time is not a list of characters as in above example. instead c = 'AM' # a string

a, b, c = list(s[:2]) + [s[2:]] # the right side here essentially becomes ['S', 'P', 'AM']
print(a)
print(b)
print(c) # 'AM'

# an easier more intuitive and simpler way to achieve the above is shown below
a, b = s[:2]
c = s[2:]
print(a)
print(b)
print(c) # 'AM'

# another simpler way is using nested sequences
(a, b), c = s[:2], s[2:]
print(a) # 'S'
print(b) # 'P'
print(c) # 'AM'

# the above is same as:
(a, b), c = ('SP', 'AM')
print(a)
print(b)
print(c)

red, blue, green = range(3)
print(red)
print(blue)
print(green)

# starred names in detail
w = [1, 2, 3, 4]
a, *b = w # first, rest
print(a) # 1
print(b) # list # [2, 3, 4]

*a, b = w # rest, last
print(a) # list # [1, 2, 3]
print(b) # this time b takes the last element and a takes the rest before it

# in the traditional slicing way this would be achieved as below
a = w[:-1], w[-1]

# when starred name is used in the middle, it collects everything between the other names listed.
a, *b, c = w
print(a) # 1
print(b) # [2, 3]
print(c) # 4

# a practical usage example of * names
L = [1, 2, 3, 4]
while L:
    front, *L = L # no manual slicing of L required
    print(front, L)

# boundary cases
#1 starred name always returns a list even if only 1 item remains.
seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a) # 1 
print(b) # 2
print(c) # 3
print(d) # [4]

#2 if nothing is left, starred name is assigned an empty list
a, b, c, d, *e = seq
print(a) # 1 
print(b) # 2
print(c) # 3
print(d) # 4
print(e) # empty list [] since nothing was left to unpack

a, b, *c, d, e = seq
print(a) # 1
print(b) # 2
print(c) # empty list [] since nothing left to unpack
print(d) # 3
print(e) # 4

*a, = seq #this works because `*a, ` is nothing but a tuple, recall parenthesis are not required. had you coded `*a = seq` you will get error as * names can only appear in a list or tuple, i..e not alone
print(a)
# NOTE a is actually a copy of seq. i.e. it is not pointing to the same object referenced by seq. because recall starred names collects everything in a list by running list(seq)
# so this is same as a = list(seq) which would also create a copy of object referenced by seq.
a[1] = 199
print(a) # changed 
print(seq) # unchanged

# multiple-target assignment
a = b = c = 'spam'
print(a, b, c)
# above is equivalent to doing:
c = 'spam'
b = c
a = b

a = b = []
b.append(42)
print(a, b) # a got changed too.

# to avoid such issues initialize mutable objects in separate lines so it creates a new object for each name. 
a = []
b = []
b.append(42)
print(a, b) # a is unchanged

# augmented assignments
a = 1
b = 2
a += b # nothing but a = a + b
print(a)

s = 'spam'
s += 'SPAM' # + concatenates the two string objects
print(s)

L = [1, 2]
L = L + [3]  # concatenation
print(L)
L.append(4) # in-place change
print(L)

L = L + [5, 6]
print(L)
L.extend([7, 8]) # NOTE that it is .extend method for appending multiple items to the list. if you used the .append() method it would add the list object [7, 8] as the new object.
print(L)
# note .extend() is faster than the concatenation approach. 
# when using augmented assignment python automatically calls the faster .extend() method on it. 
L += [10, 11] # even though it look like it would be using the concatenation approach, it is actually using .extend() behind the scenes.
print(L)

# be careful when dealing with shared reference on mutable objects though
L = [1, 2]
M = L
L = L + [3, 4] # creating a new object.
print(L, M) # L is changed, not M

L = [1, 2]
M = L
L += [3, 4] # in-place extend
print(L, M) # M changed too 

# another way to make in-place changes
L = [1, 2]
M = L
L[len(L): ] = [3, 4, 5] # changed in place
print(L, M) # both changed

# common python beginner mistake:
L = [1, 2]
L = L.append(3) # append() is a method of the list object. it changes the list in-place and it returns None
print(L) # prints None, you have lost your list L in doing so!!
# same thing applies to other methods that change mutable objects in place.

# printing in python
print() # displays a blank line

print('hello world')
x = 50
y = 'spam'
z = [43.21, 'ham']
print(x, y, z) # every object is sep by single space as sep=" "
print(x, y, z, sep="-")

print(x, y, 'banana republic', end=""); print(47.668)
print(x, y, z, sep="+", end="...!")

# output redirection
print(x, y, z, file=open('print_tests.txt', 'w'))

print(open('print_tests.txt', 'r').read()) # this is just reading from a file

text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)
print('%s: %-.4f, %05d' % ('Result', -83.14159, 42764676))

import sys
sys.stdout = open('log.txt', 'a') # append mode
print(x, y, z)
print('hello world')


