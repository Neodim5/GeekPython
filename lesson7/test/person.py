class Person():
    def __init__(self, attrs: dict):
        self._attributes = attrs

    def __del__(self):
        print("Person is removed")

    def __str__(self):
        return f"Person: {self._attributes['first_name']} {self._attributes['last_name']}"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if item != 'age':
            return self._attributes[item]
        else:
            return None
    def __setattr__(self, key, value):
        if '_attributes' in self.__dict__:
            self._attributes[key] = value
        else:
            super().__setattr__(key, value)


dim = Person({"first_name": "Dim", "last_name": "Neo", "age": 35})
oxy = Person({"first_name": "Oxy", "last_name": "Neo", "age": 35})
# del dim

#print(dim._attributes['first_name'])
print(dim)
print(oxy)

users = [dim, oxy]
print(users)

print(dim['first_name'])
print(oxy['first_name'])
print(dim['age'])
print(oxy['age'])

dim.job = "DevOps"
print(dim['job'])
