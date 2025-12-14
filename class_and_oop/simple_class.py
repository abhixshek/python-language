class rec: pass # an empty namespace object

# or alternatively 
class rec: ... # ellipses. read looping_constructs note in obsidian for more on this. but all this expression does is NOTHING. so it can act as a replacement for the keyword pass

rec.name = 'bob'
rec.age = 40

print(rec.name)

# this way of creating an empty class and then assigning attributes to it to belong to this namespace is similar to a "struct" in C.
# note that what we have done above could also be achieved by simply using a python dictionary. Just that you cannot use the obj.attribute notation but you can do obj[attribute] to fetch an attribute.

# NOTICE that we have not created any instance of this class yet. We are able to explicitly assign new attributes to the class, because classes are objects in their own right.

x = rec()
y = rec()

print(x.name) # name attribute is available in the instance of rec because of inheritance
print(y.name) # same value as x.name

# because we created name as a class attribute, this attribute is the name for both the instances x and y.

x.name = "spam" # by doing this assignment, you have created a name attribute for this instance and remember that attribute search begins from the instance object then to its classes and then to its superclasses
print(x.name) # spam
print(y.name) # still prints bob. because when you change x.name, you are changing the object to which x.name references. so now it references the object "spam" but y.name still references the object "bob"

# infact, the attributes of a namespace object are usually implemented as dictionaries, and class inheritance trees are (generally speaking) just dictionaries with links to other dictionaries.
print(rec.__dict__.keys())
print()
print(x.__dict__.keys())
print(y.__dict__.keys())

# each instance has a link to its class for inheritance, using the __class__ attribute
print(x.__class__) # rec

from third_example import ThirdClass

print(ThirdClass.__class__)
print(ThirdClass.__bases__)
# __class__ and __bases__ are the two attributes how class trees are literally represented in memory by Python.

# defining a function outside a class
def upperName(self):
    return self.name.upper() # this function expects self to have an attribute name. but it does not restrict what self can be. There is nothing about a class here yet.

print(upperName(x)) # called as a normal function. notice that x has the interface required by the function which is that it should have a name attribute.
print(x.name) # unchanged. because in the above function we did not assign the result back to self.name. we just returned it.

rec.method = upperName
print(x.method())
print(x.name) # unchanged

print(y.method())

# call the method using the class name
print(rec.method(x))


