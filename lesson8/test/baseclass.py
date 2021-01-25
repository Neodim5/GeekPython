class MyObject:
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Person(MyObject):
    def __init__(self, name):
        self.name = name
        self.age = 10

dim = Person('Dim')
print(dim)