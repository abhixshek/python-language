class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # add __str__ method for printing objects
    def __str__(self):
        return '[Person: %s, %s]' %(self.name, self.pay)


class Manager(Person):
        def __init__(self, name, pay=0):
            Person.__init__(self, name, job='mgr', pay=pay)

        def giveRaise(self, percent, bonus=0.10):
            Person.giveRaise(self, percent + bonus)


if __name__ == "__main__":
    henry = Person('Henry Ford', 'MLE', 30)
    john = Person('John Harris')
    tom = Manager('Tommy Hilfiger', 50_000)
    print(henry)
    print(tom)

    print(henry.__class__)
    print(henry.__class__.__name__)
    print(tom.__class__)

    print(list(henry.__dict__)) # name, pay, job. notice its everything that was assigned as `self.attr`
    print(list(tom.__dict__)) # name, pay, job
    print(tom.__dict__) # {'name': 'Tommy Hilfiger', 'job': 'mgr', 'pay': 50000}

    print(Person.__dict__) # giveRaise, lastName, __init__, etc
    print(Manager.__dict__)

    print(dir(tom)) # self attributes + inherited attributes







