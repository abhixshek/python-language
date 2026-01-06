class Person:
    # constructor method
    def __init__(self, name, job=None, pay=0): # other than being automatically getting called at object creation time,
        # this method/function is no different than any other function you have ever studied
        self.name = name
        self.job = job
        self.pay = pay # self is the new instance object

    # add methods to encapsulate operations for maintainability 
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) # if in future, the logic/calculation changes, the change will be required here only, not anywhere else in code
        # example, every pay raise must have a prior approval with it, etc.


if __name__ == "__main__":
    p1 = Person(name='John Harris')
    p2 = Person('Henry Ford', 'MLE', 30)
    print(p1.name, p1.job, p1.pay)
    print(p2.name, p2.job, p2.pay)
    
    # each of p1 and p2 are independent records of information. Technically, called namespace objects.

    print(p1.name.split()[-1]) # print surname of the person
    p2.pay *= 1.10 # give this object a 10% raise
    print(p2.pay) # in a sense, our class instances are mutable objects, as we are able to update pay in-place

    henry = Person('Henry Ford', 'MLE', 30)
    john = Person('John Harris')
    
    print(john.lastName())
    henry.giveRaise(0.1)
    print(henry.pay)

