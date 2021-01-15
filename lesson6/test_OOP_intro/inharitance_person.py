class Person:
    _first_name: str
    _last_name: str

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def fullname(self):
        return f"{self._first_name} {self._last_name}"

class User(Person):
    login: str
    password: str

    def login(self):
        print(f"Welcome, {self.fullname()}!")


#john = Person("Jone", "Doe")
john = User('Dim', 'Neo')
john.login()
