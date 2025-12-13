from first_example import FirstClass


class SecondClass(FirstClass): # inherits setdata
    def display(self): # changed display
        print('Current value = "%s"' %self.data)

z = SecondClass()

z.setdata("BLR")
z.display()

# NOTE, that FirstClass is unaffected by SecondClass, i.e., a superclass is unaffected by what a subclass is doing/changing.
# ex:
o1 = FirstClass()
o1.setdata("spam")
o1.display() # still uses display as defined in FirstClass

