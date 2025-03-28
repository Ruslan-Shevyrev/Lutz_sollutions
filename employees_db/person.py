class Person:
    def __init__(self, pk: str, name: str, age: int, pay: float = 0.0, job: str = None):
        self.pk = pk
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)

    def last_name(self) -> str:
        return self.name.split()[-1]

    def give_raise(self, percent: float):
        self.pay *= (1.0+percent)


if __name__ == '__main__':
    bob = Person('bob', 'Bob Smith', 42, 30000.0, 'software engineer')
    sue = Person('sue', 'Sue Jones', 40, 40000.0, 'hardware engineer')
    print(bob)
    print(sue)
    print(bob.last_name())
    print(sue.last_name())
    print('Sue\'s pay before raise: ' + str(sue.pay))
    sue.give_raise(.10)
    print('Sue\'s pay after raise: ' + str(sue.pay))
