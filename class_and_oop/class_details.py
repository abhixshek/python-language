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




