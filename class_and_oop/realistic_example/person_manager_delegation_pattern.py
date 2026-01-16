# inheritance is not the only way to design or combine classes.
# another approach is called composites, where you embed one object inside another.

# the below pattern is specifically called a delegation - a composite-based structure that manages a wrapped object and
# propagates method calls to it. 

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' %(self.name, self.pay)
    
    def __getattr__(self, attr):
        return "this attribute you are trying to fetch is not defined."


class Manager: # NOTE, no inheritance used here
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay) # embed a Person object
    
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus) # intercept and delegate
    
    def __getattr__(self, attr):
    # __getattr__ is called whenever an attribute does not exist in an instance when instance.attr is run
        return getattr(self.person, attr)
        # getattr(instance, attr: str) is a built-in function that can be used as an alternative to instance.attr
        # and also supports passing a default to return if attr is not found.
    
    def __str__(self):
        return str(self.person) # str(obj) calls that object's __str__() method


if __name__ == "__main__":
    henry = Person('Henry Ford', 'MLE', 30)
    john = Person('John Harris')
    tom = Manager('Tommy Hilfiger', 50_000)
    print(henry)
    print(john)
    print(tom)
    
    print(tom.pay) # NOTICE how pay variable was never really defined in Manager, its been dispatched using __getattr__
    print(tom.leaves) # again, leaves is not defined for tom. inheritance we are not doing any way so there is no inheritance tree
    # to be searched in. and therefore the __getattr__ method gets called. that in turn calls getattr() on the person object
    # getattr() internally calls the __getattr__ method of the passed in object. which means it calls the __getattr__ method
    # we defined in the Person class.

    # this composite pattern did not really seem intuitive/appropriate to be used in this Person and Manager example
    # inheritance was the right way to go about it. 
    # although this composite pattern can be useful in applications where there is more limited interaction
    # between two types of objects. see department_composition.py
