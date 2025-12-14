from first_example import FirstClass


class SecondClass(FirstClass): # inherits setdata
    def display(self): # changed display
        print('Current value = "%s"' %self.data)

if __name__ == "__main__":
    z = SecondClass()

    z.setdata("BLR")
    z.display()

    # NOTE, that FirstClass is unaffected by SecondClass, i.e., a superclass is unaffected by what a subclass is doing/changing.
    # ex:
    o1 = FirstClass()
    o1.setdata("spam")
    o1.display() # still uses display as defined in FirstClass

    print(dir(o1))
    print(o1) # implements the default behaviour of __str__() of python classes
    print(o1.__str__()) # same output as above. see more on __str__ in third_example.py

