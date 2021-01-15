class Human:
    age = int
    first_name = str
    last_name = str
    weight = int

    def __init__(self, first_name, last_name, age, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight

    # def __init__(self):

    def info(self):
        print(f"Im {self.first_name}, age: {self.age}, weight: {self.weight}")


john = Human('John', 'Doe', 30, 90)
arture = Human('Artur', 'Doe', 40)

john.info()
arture.info()

'''
print(john, arture)
john.age = 30
john.first_name = "John"
john.last_name = "Doe"

arture.age = 40
arture.first_name = "Artur"
arture.last_name = "Doe"

# print(john.age, arture.age)
print(john.first_name, john.last_name, john.age, john.weight)
print(arture.first_name, arture.last_name, arture.age, arture.weight)

john.info()
arture.info()
'''