class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self) -> str:
        return 'Person: %s, %s' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__=='__main__':
    # bob = Person("Bob Smith")
    # sue = Person("Sue Jones", job='dev', pay=100000)
    # print(bob)
    # print(sue)
    # print(bob.lastName(), sue.lastName())
    # sue.giveRaise(.10)
    # print(sue.pay)
    
    from number import Number
    x = Number(5)
    y = x - 2
    print(y.data)