name = "Dim"
print(hash(name))
value = [1, 2, 3]
#print(hash(value))

tup = (1, 2, 3)
print(hash(tup))

class TestClass:
    fist_name: str
    values: list

    def __init__(self, attr):
        self.fist_name = attr
        self.values = []

    def __hash__(self):
        return hash(self.fist_name)



a=TestClass("Dim")
a.fist_name = "Invalid"
print(hash(a))
print(hash(TestClass("Dim")))
