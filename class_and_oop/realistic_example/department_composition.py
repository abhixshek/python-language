# this code uses both inheritance and composition—Department is a composite
# that embeds and controls other objects to aggregate, but the embedded Person 
# and Manager objects themselves use inheritance to customize.

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


class Manager(Person):
        def __init__(self, name, pay=0): # redefine constructor
            Person.__init__(self, name, job='mgr', pay=pay) # run original with 'mgr'

        def giveRaise(self, percent, bonus=0.10):
            Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    
    def addMember(self, person):
        self.members.append(person)
    
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    
    def showAll(self):
        for person in self.members:
            print(person)
    

if __name__ == "__main__":
    henry = Person('Henry Ford', 'MLE', 30)
    john = Person('John Harris')
    tom = Manager('Tommy Hilfiger', 50_000)

    development = Department(henry, john) # Embed objects in a composite
    development.addMember(tom)

    development.giveRaises(.10) # Runs embedded objects' giveRaise

    development.showAll()



