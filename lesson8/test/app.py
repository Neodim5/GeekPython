class CarFactory:
    model = 'UAZ'
    common_price = 650000

    def build(self, count=1):
        cars = []

        for x in range(count):
            cars.append(
                Car(self.model, self.common_price)
            )

        return cars


class CarStock:
    max_count: int
    cars: list


    def __init__(self, count=0):
        self.max_count = count
        self.cars = []

    def store(self, cars: list):
        # проверять self.max_count (cars)
        if len(self.cars) >= self.max_count:
            raise CapacityExeption(len(self.cars), len(self.cars) + len(cars))
        elif len(cars) > (self.max_count - len(self.cars)):
            raise CapacityExeption(self.max_count, len(self.cars) + len(cars))

        self.cars.extend(cars)

class CapacityExeption(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return  f"Не достаточно места на складе. Фактически = {self.current}, необходимо = {self.needle}"




class NotEnMoneyExeption(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return  f"Не достаточно денег. Наличных = {self.current}, необходимо = {self.needle}"


class Car:
    medel: str
    price: int

    def __init__(self, medel, price):
        self.medel = medel
        self.price = price


class Custome:
    money: int

    def __init__(self, money):
        self.money = money

    def buy(self, car: Car):
        # проверять текущий баланс
        if car.price > self.money:
            raise NotEnMoneyExeption(self.money, car.price)
        self.money -= car.price

#Создаем завод
factory = CarFactory()

try:
    #Создаем склад
    stock = CarStock(1)
except CapacityExeption as exeptionStore:
    print(f"")
#покупатель с деньгами
dim = Custome(100000)

#создаем определенное количество автомобилей на заводе
car_list = factory.build(4)
#разместим машины в магазине
stock.store(car_list)

try:
    #покопаем авто
    dim.buy(stock.cars[1])
except NotEnMoneyExeption as exception:
    print(f"для покупки вам не хватает -  {exception.needle - exception.current} руб")

print(dim.money)