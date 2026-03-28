class Super:
    def hello(self):
        self.data1 = 'hello world'

class Sub(Super):
    def hola(self):
        self.data2 = 'Hola, India'

x = Sub()
print(x.__dict__) # instance namespace. currently an empty dict

print(x.__class__) # class that x is an instance of. in this case Sub.

print(Sub.__bases__) # tuple of classes the Sub class inherits from. It lists just the direct parents. if this class is at the 3rd level in an inheritance tree, __bases__ is only going 
# to return the 2nd level classes. In other words, the parent of parents can only be known through one of the classes' at the 2nd level and its __bases__ attribute

print(Super.__bases__) # class object

print(Sub.__dict__.keys()) # __module__, hola, __doc__
print(Super.__dict__.keys()) # __module__, __doc__, hello, __weakref__

y = Sub()
print(y.__dict__) # empty

x.hello()
print(x.__dict__) # has data1 now

x.hola()
print(x.__dict__) # has data1 and data2

print(y.__dict__) # still has an empty namespace.
# each instance has an independent namespace dictionary, which starts out empty and can record completely different attributes than
# those recorded by the namespace dictionaries of other instances of the same class.

print(x.data2, x.__dict__['data2'])

x.data100 = 'python is best'
print(x.data100)

print(x.__dict__)

x.__dict__['data5'] = 'ham'
print(x.__dict__)

# dir built-in function uses these same _dict__ dictionaries and includes some system attributes too in the result.
print(dir(Super))
print(dir(Sub))
print(dir(x))
print(dir(y))

print(Sub.__bases__)
print(Super.__bases__)
