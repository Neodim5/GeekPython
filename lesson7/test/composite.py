from abc import ABC, abstractmethod


class AbstractUser(ABC):
    @abstractmethod
    def sho_name(self):
        pass


class Person(AbstractUser):

    def sho_name(self):
        print(f"it a person")


class User(AbstractUser):

    def sho_name(self):
        print(f"it a User")

class CompositeUser(AbstractUser):
    def __init__(self, children: list):
        self.children = children

    def sho_name(self):
        for item in self.children:
            item.sho_name()

a=Person()
b=User()

compositer = CompositeUser([a, b])
compositer.sho_name()