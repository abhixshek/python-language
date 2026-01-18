class C1:
    def printer(self):
        print(5)

i1 = C1()
i2 = C1()

i1.printer() # 5
i2.printer() # 5

def new_printer():
    print(10)

i1.printer = new_printer

i1.printer() # 10
i2.printer() # 5

def new_printer(self):
    print(55)

C1.printer = new_printer

i2.printer() # 55
i1.printer() # 10

# NOTE, how the first time we defined new_printer, we did not pass self, while in the above definition we have passed self.
# this is because the former one was assigned as an attribute directly to the instance, so it does not really act as a class method, rather its just an object which happens to be callable.
# while in the latter case, we updated the "class" C1's method and it MUST have a self argument

C1.b = 33
i3 = C1()

print(i1.b) # 33
print(i2.b) # 33
print(i3.b) # 33
# That is all instances of C1 class have access to the attribute b even though it is created after i1 and i2 instances were already created. This is because the attribute search will always happen
# in the class tree dynamically, in other words, i1 and i2 are NOT creating a separate local copies of C1 for themselves.

