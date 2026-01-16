import shelve


if __name__ == "__main__":
    db = shelve.open('persondb') # open the shelve
    for key in sorted(db):
        print(key, '\t=>', db[key])
    
    sue = db['Sue Jones']
    sue.giveRaise(.20)
    db['Sue Jones'] = sue
    
    db.close()
