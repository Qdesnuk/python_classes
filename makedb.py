from main import Person

bob = Person("Bob Smith")
sue = Person("Sue Jones", job='dev', pay=100000)
tom = Person("Tom Jones", pay=100000)

import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()