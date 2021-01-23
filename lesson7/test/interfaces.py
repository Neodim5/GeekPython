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



dim = Person()
oxy = User()

dim.sho_name()
oxy.sho_name()
