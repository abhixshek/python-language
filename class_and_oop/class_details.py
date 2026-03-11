import realistic_example.person
class SharedData:
    spam = 42

x = SharedData()
y = SharedData()

print(x.spam, y.spam) # prints 42, 42

y.spam = 99 # only changes for y
# Assignments to instance attributes create or change the names
# in the instance, rather than in the shared class.
# y.spam attaches the name to y itself and therefore from now on y.spam will not trigger inheritance search.
# in general, inheritance searches occur only on attribute references, not on assignment
z = SharedData()
print(x.spam, y.spam, z.spam) # prints 42, 99, 42. 

SharedData.spam = 33
print(x.spam, y.spam, z.spam) # prints 33, 99, 33. 

class MixedNames: # Define class
    data = 'spam' # Assign class attr
    def __init__(self, value): # Assign method name
        self.data = value # Assign instance attr
    def display(self):
        print(self.data, MixedNames.data) # Instance attr, class attr

a, b, c = MixedNames(100), MixedNames('hello'), MixedNames(55)
print(a.data, b.data, c.data) # 100, hello, 55. 

a.display(); b.display(); c.display()
# self.data differs for each object, but MixedNames.data is the same.



class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)

x = NextClass()
x.printer('hello')
print(x.message)
x.printer('jonty')
print(x.message)

# another way to call class methods:
NextClass.printer(x, 'hello world')
print(x.message) # this instance's message attribute was changed in the above call.


# calling superclass' constructor
class Super:
    def __init__(self, x):
        self.x = x

class Sub(Super):
    def __init__(self, x, y):
        self.y = y
        Super.__init__(self, x)

i = Sub(3, 5)
print(i.x, i.y)


class Super:
    def method(self):
        print('in Super.method')

class Sub:
    def method(self): # override method
        print('Starting Sub.method') # add actions here
        Super.method(self) # run default action
        print('ending Sub.method')

# this way Sub only extends Super.method's behaviour, rather than replacing it completely.
a = Sub()
a.method()

x = Super()
x.method() # runs super.method


print('\n\n### Abstract classes')
# syntax to indicate/create abstract super class (base class)
from abc import ABCMeta, abstractmethod
class Super(metaclass=ABCMeta): # metaclass is a keyword-only argument in this class header.
    def delegate(self):
        self.action()

    @abstractmethod # decorator, studied later
    def action(self):
        pass
        
# the effect of this is that you CANNOT make an instance unless the method is defined lower in the class tree.

try:
    a = Super()
except TypeError as e: # the exception is triggered and this except clause gets run
    print(e)

class Sub(Super): pass

try:
    x = Sub()
except TypeError as e: # again, still the exception is triggered because the abstract method `action` is still the active method in the class tree
    print(e)

class Sub(Super):
    def action(self):
        pass # ideally you better do something else, but I have written pass to demonstrate that `action` defined here does not necessarily need to do anything to get rid of the abstractness of the Super class;
    # `abstract` method. The def here alone solves the issue.

y = Sub() # runs normally.

class Sub(Super):
    def action(self):
        print('Running action of Sub')

y = Sub()
y.delegate()



