a = [] # empty list
print(type(a))

a = [53, 23, 7, 21]
print(a)
print(len(a)) # 4
r = a + [1, 4, 5] # concatenation. returns a new list
print(r)
print(len(r))
print(a) # notice a was not changed.

t = a * 3 # repetition
print(t)
print(len(t))
print(a) # a was not changed

# r = [1, 2, 3] + "45" # gives TypeError. you cant concatenate a list object and a str object

a = [5,7,3,87,1,8,5]
print(a)
# iteration
for i in a:
    print(i, end=" ")

print()
print(3 in a) # membership

r = [i * 2 for i in a] # list comprehension
print(r)

a = list(range(-4, 4))
print(a)
r = list(map(abs, a)) # map generator function applies the specified function to each item in the iterable
print(r)

print(a[0]) # indexing
print(a[-2])
print(a[2:4]) # slicing, includes index 2 and 3, not 4

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ] # nested list, acts like a 2D array
print(matrix)
print(matrix[1])
print(matrix[1][1])


# changing lists in-place
a = [534, 78, 232, 99, 1, 2, 5]
print(a)
a[1] = 100
print(a)
a[2:4] = [340, 33]
print(a)
a[1:2] = [7, 8, 9] # [1:2] is just index 1 because 2 will not be included (right bound). also notice that on the left of the = we have just 1 index being assigned to but the RHS has items more than that
# and thats okay. the length of the slice on the left DOES NOT HAVE TO MATCH the RHS length
print(a)
a[1:4] = a[2:5]
print(a)

print('List method calls')
# list method calls
a = [534, 78, 232, 99, 1, 2, 5]
print(a)
a.append(33) # adds another item at the end in-place. this is similar to `a + [33]` but faster. and also the concatenation operation creates a new list while the append method changes list in-place
print(a)

a.sort() # sorts the list in-place, by default in ascending order.
print(a) # do not do the mistake a = a.sort() because the sort method changes the list in-place and does not return anything (i.e. returns None). and hence such a statement would make `a` become None

a = [75,3,8,5,3,7,7,1]
print(a)
a.sort(reverse=True) # reverse=True implies descending order
print(a)

a = ['aBe', 'ABD', 'abc']
print(a)
a.sort()
print(a) # a is sorted. ['ABD', 'aBe', 'abc']

# you can pass a "single argument function" like str.lower() to the `key` argument of sort() method to enforce your ordering/comparison logic.
a = ['aBe', 'ABD', 'abc']
a.sort(key=str.lower) # it first applies str.lower to the list elements and then compares which one is smaller. also note that str.lower is applied only for comparison purpose.
# the original elements of the list are unchanged after sorting.
print(a) # ['abc', 'ABD', 'aBe']

# NOTE because mixed type comparisons are not allowed except within numeric types, you cannot sort a list with mixed types like int and str

a = ['aBe', 'ABD', 'abc']
print(a)
w = sorted(a, key=str.lower) # sorted() built-in returns a new sorted list and does not change the list in-place
print(w)
print(a) # a is unchanged

a = [56,8,34,8,4,34]
print(a)
a.reverse() # reverses the list in-place. NOTE that reversing is not sorting
print(a)
q = list(reversed(a)) # reversed() is a built-in. but it is a generator so it must be wrapped in a list() call to return the complete list
print(q)

a = [56, 3, 5]
a.extend([8, 9]) # use .extend() to insert multiple items at the end of the list
print(a)

r = a.pop() # pops the item at the end of the list and updates the list in-place
print(r) # the item at the last index
print(a) # a is updated with the last item removed now

# LIFO stack data structure using pop and append
a = []
a.append(1) # push onto stack
a.append(9)
print(a)
a.pop() # pop off stack
print(a) # [1]

# The pop method also accepts an optional offset of the item to be deleted and returned (the default is the last item). 

a = [4, 6, 8, 2, 4, 0, 9, 10]
print(a)
a.insert(1, 55) # insert 55 at index 1. note that it is not replacing what is already at index 1. it will push [1:] existing elements one offset to the right
print(a)

i = a.index(9) # returns the index of the value passed. if value does not exist in the list, it gives ValueError
print(i)

a.remove(4) # note that there were two 4s in the list. it removed the first occurence
print(a) # a is updated

a.pop(3) # delete by position
print(a)

# deleting an item or slice
a = [4, 6, 8, 2, 4, 0, 9, 10]
print(a)
del a[1] # a is updated in-place
print(a)
del a[4:6] # a is updated in-place
print(a)
# this is same as running a[4:6] = []
a = [4, 6, 8, 2, 4, 0, 9, 10]
print(a)
del a[1]
a[4:6] = []
print(a)
# NOTE that if you assign an empty list to a single offset (not a slice) then it will mean replacing the item at the offset with an empty list
a = [4, 7, 9, 2, 4, 1]
print(a)
a[1] = []
print(a) # [4, [], 9, 2, 4, 1]



### dictionaries
d = {} # empty dict
d = {'name': 'john', 'dob': '2000-12-12', 'height': 170.25}
print(d)
print(type(d))
print(d['height']) # indexing by key
# there is no fixed left-to-right ordering of keys. Python randomizes them, and so their position is not based on how you type them out. therefore there is no notion of positional indexing in dicts.
# this is to allow for fast key lookup (a.k.a hashing)

r = 'name' in d # key membership test
print(r) # True

print(len(d)) # no. of items stored in the dictionary or in other words, the length of its keys list

w = d.keys()
print(w)
print(type(w)) # <class 'dict_keys'>

# NOTE that d.key() is not subscriptable. its iterable but not subscriptable/indexable. because d.keys() is iterator. 
# to do that run a list() call
w = list(d.keys())
print(w)
print(w[1])

d['name'] = ['john', 'makensy'] # updating the value of a key. also assigning a list as value makes this dictionary nested. 
print(d)

del d['height'] # updates the dict in-place as dict are mutable
print(d)
d['weight'] = 65
print(d)

v = list(d.values())
print(v)
r = list(d.items()) # list of tuples of key, value pairs
print(r)

# to avoid getting a KeyError when indexing a non-existent key, use .get() method
print(d.get('weight')) # key exists so we get the value
print(d.get('pay')) # non-existent key, returns None by default
print(d.get('pay', 'unknown')) # prints unknown

d1 = {'a': 10, 'b': 15}
d2 = {'e': 22, 'b': 42}
print(d1)
print(d2)
d1.update(d2) # updates d1 in-place with new key-value pairs from d2. does not return anything. if a key already exists in d1, it updates with the value found in d2.
print(d1) # value of b got updated to 42 as found in d2

r = d1.pop('a') # deletes the key 'a' from d1 and returns the associated value.
print(r)
print(d1)
# if you try to pop a key that does not exist in the dictionary, you will get a KeyError
d3 = d1 # shared references to the same dictionary object
del d3['b']
print(d3)
print(d1) # both d1 and d3 updated as both point to the same object

d4 = d1.copy() # creates a copy
d4['g'] = 110
print(d4) # updated
print(d1) # un-changed





