from person_final import Person, Manager


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Radcliff', 50000)

import shelve
db = shelve.open('persondb') # filename where objects will be stored
for object in (bob, sue, tom):
    db[object.name] = object # store object on shelve by key
    # in shelve, the only rule is that keys must be strings only.

db.close()

