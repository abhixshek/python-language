import shelve


if __name__ == "__main__":
    db = shelve.open('persondb')
    print(list(db.keys()))
    bob = db['Bob Smith']
    tommy = db['Tom Radcliff']
    print(bob)
    print(tommy)
    print(bob.lastName()) # NOTE, that we don’t have to import our Person or Manager classes here in order to load or use our stored objects.
    tommy.giveRaise(.20) # 0.2 + default bonus (0.10)
    print(tommy)

    print(len(db)) # 3 records are stored

    db.close()
