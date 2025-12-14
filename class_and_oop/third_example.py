from second_example import SecondClass


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self): # on print(self), str()
        return '[ThirdClass: %s]' %self.data

    def mul(self, other):
        self.data *= other

if __name__ == "__main__":
    a = ThirdClass('abc') # __init__ called
    a.display() # inherited method display from SecondClass
    a.setdata('xyz') # notice how you can call setdata as well which does not appear in ThirdClass or SecondClass but appears in FirstClass which is SecondClass is inheriting from
    # to avoid making such explicit call to assign data to `a`, we have coded the __init__ method. It automatically takes care of assigning data at object construction time
    # i.e., ThirdClass('abc')
    a.display()

    print(a) # uses obj.__str__()

    b = a + 'spam' # in a + 'spam', what happens is a is passed as self and spam is passed as other to the function __add__ 
    b.display()

    print(b) # notice that now that we are able to print b directly using print() statements, we dont really need the display() method
    # infact, to avoid coding display() only we have now got __str__(), which is automatically called in print(obj) calls.


    a.mul(3) # changes a in-place
    print(a)

    print(dir(a))
