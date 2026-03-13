X = 5 # global (module) name/attribute (X, or namespace_concepts.X)

def f():
    print(X)  # access global X (5)

def g():
    X = 22 # local (function) variable (X, hides module X)
    print(X) # 22

class C:
    X = 33 # class attribute (C.X)
    def m(self):
        X = 44 # local variable in method (X)
        self.X = 55 # instance attribute (instace.X)


if __name__ == "__main__":
    print(X) # prints 5. 
    f() # 5
    g() # 22: local
    print(X) # 5

    obj = C()
    print(obj.X) # 33

    obj.m() # notice in the method m we attach an attribute X to self.

    print(obj.X) # 55. now its the instance attribute which comes first in the inheritance search

    print(C.X) # 33

    # print(C.m.X) # cannot access local variable in a function like this.
    # print(g.X) # cannot access local variable in a function like this. X inside g is visible only inside g.

