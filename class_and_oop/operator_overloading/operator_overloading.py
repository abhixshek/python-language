from number import Number # fetch Number class from module


X = Number(6) # Number.__init__(X, 6)
Y = X - 2 # Number.__sub__(X, 2)
print(Y.data) # Y is a new Number instance


# __getitem__ and __setitem__
class Indexer:
    def __getitem__(self, index):
        return index ** 2 # returns the square of index passed

X = Indexer()
print(X[3]) # X[i] calls X.__getitem__(i)
print(X[4] + 3) # 19


# intercepting slices
L = [5, 6, 7, 8, 9]
print(L[2:4]) # [7, 8]
print(L[1:]) # [6, 7, 8, 9]
print(L[:-1]) # [5, 6, 7, 8]
print(L[::2]) # [5, 7, 9]
# slice syntax is really just syntactic sugar for indexing with a slice object. NOTICE how the below results in the prints are all same as the above results
print(L[slice(2, 4)]) # [7, 8]
print(L[slice(1,None)]) # [6, 7, 8, 9]
print(L[slice(None, -1)]) # [5, 6, 7, 8]
print(L[slice(None, None, 2)]) # [5, 7, 9]

# our previous Indexer class cannot handle slicing as it is since the way it is defined, it is expecting an integer(index)
class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index): # called for index or slice
        print('getitem:', index)
        return self.data[index] # perform index or slice

print('Indexing and slicing using __getitem__')
X = Indexer()
print(X[0]) # indexing sends __getitem__ an integer
print(X[1])
print(X[-1])

print(X[2:4]) # slicing sends __getitem__ a slice object
print(X[1:])
print(X[:-1])
print(X[::2])
print(X[:100])

def __setitem__(self, index, value): # intercept index or slice assignment
    self.data[index] = value # assign index or slice

Indexer.__setitem__ = __setitem__ # adding a __setitem__ method to our class

a = [4, 52, 67, 4, 3]
print(a)
print(a[1:3])
try:
    a[1:3] = 77 # cannot assign a single object to a slice. gives TypeError: must assign iterable to extended slice
except TypeError as e:
    print(e)
# even a[1:2] = 88 is not possible even though 1:2 results in just index 1 as right bound is not included in slicing
# the result of a[1:2] is still a list(iterable) and not a single object(like using a[1])
# therefore you need to have an iterable on the right side of assignment as well

a[1:3] = (9, 2) # notice RHS is a tuple because you can pass any iterable, not necessarily a list
print(a)

a[1:3] = (9, 2, 66) # 1:3 results in only 1 and 2, but passing more than 2 on the right side of = is accepted and the list is expanded accordingly
print(a) # note that a[3] did not get overwritten, instead it has been pushed to the right to index 4

print(X.data)
X[1:3] = [100, 200]
print(X.data)
X[3] = 786
print(X.data)


class R:
    def __index__(self): # somewhat confusing name __index__, but the value returned by this method is what is used when you pass a non-integer object as an index inside []
        # hex(), bin(), oct() also use this method to identify what is the integer value of an object and then convert it into hexadecimal, binary, etc format.
        return 255

X = R()
print(('C' * 300)[X])
print(('C' * 260)[X:])

# __getitem__ can also be used in iterations
class stepper:
    def __getitem__(self, i):
        return self.data[i]

X = stepper() # X is a stepper object
X.data = "Spam"

print(X[1]) # indexing calls __getitem__

for item in X: # for loop calls __getitem__
    print(item, end=' ')

print()
print('p' in X) # in membership test
print([c for c in X]) # list comprehension
print(list(map(str.upper, X)))
a, b, c, d = X
print(a, b, c, d)
print(list(X), tuple(X), '-'.join(X))

# although __getitem__ works for iteration, its really a fallback technique. prefer using __iter__ method for all iteration contexts
class Squares:
    def __init__(self, start, stop): # save state when created
        self.value = start - 1
        self.stop = stop
    def __iter__(self): # get iterator object on iter
        return self
    def __next__(self): # return a square on each iteration
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5): # `for` calls iter(), which calls __iter__()
    print(i, end=' ') # each iteration calls __next__

print()
X = Squares(5, 10)
I = iter(X)
print(I is X) # True
print(next(I)) # 25
print(I.__next__()) # 36
print(X.__next__()) # 49

# NOTE, just because the above X class implements the iteration protocol using __iter__ and __next__ does not mean that you can do X[i]
# to do indexing you are still going to require __getitem__

# while all other iteration contexts like membership tests, type constructors, list comprehension, etc apply with __iter__ as well
# we have to be careful to note that a class's iter may be designed for a single traversal only.
# ex:
Y = Squares(12, 16)
print([n for n in Y]) # [144, 169, 196, 225, 256]
print([n for n in Y]) # [], now its empty because iteration is exhausted.

# multiple iterators on one object
# example of built-in type
s = 'spam'
for x in s:
    for y in s:
        print(x + y, end=' ')
# each loop grabs an iterator from the string by calling `iter` to get an independent iterator.
print() 

# when coding user-defined iterators with classes, it is upto us to decide if we will support single active iteration or many.
# to support multiple iterators, `__iter__` needs to define a new stateful object for the iterator, instead of returning `self`.

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped # iterator state information
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped): # terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # else return and skip
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped): # save item to be used
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped) # new iterator each time

alpha = 'abcdef'
skipper = SkipObject(alpha) # make container object
I = iter(skipper) # make an iterator on it
print(next(I), next(I), next(I)) # visits offsets 0, 2, 4

for x in skipper: # `for` calls __iter__ automatically
    for y in skipper: # nested fors call __iter__ again each time
        print(x + y, end=' ') # each iterator has its own state, offset

print()




        


