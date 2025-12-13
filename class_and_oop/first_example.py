class FirstClass: # define a class object
    def setdata(self, value): # define class methods
        self.data = value # self is the instance
    def display(self):
        print(self.data) # per instance

    # as we know def statement creates a name, in this case setdata and display
    # since these names appear inside a class statement, they are attributes of this class and live in the class statement's scope
    # and can be accessed using FirstClass.setdata and FirstClass.display

if __name__ == "__main__":
    o1 = FirstClass() # make an instance. each instance gets its own namespace.
    o2 = FirstClass()

    # In OOP language, we say o1 "is a" FirstClass. similarly o2 is a FirstClass

    o1.setdata("Harry") # calling a method. self is o1 here.
    o2.setdata(99.5) # self is o2.

    o1.display() # prints Harry
    o2.display() # prints 99.5

    o1.data = "india" # another way to set attributes
    o1.display() # prints india

    o1.anothername = "spam" # notice how we can dynamically assign any attributes we want. It does not neccessarily have to be present in the class definition
    print(o1.anothername)
