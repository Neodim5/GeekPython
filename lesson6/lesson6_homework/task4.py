__author__ = 'Neklyudov Dmitry'
'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда). Опишите несколько 
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать
 текущую скорость автомобиля. Для классов TownCar и WorkCar 
 переопределите метод show_speed. При значении скорости свыше 60 (TownCar) 
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class Car:
    '''
    Базовый класс автомобилей
    '''
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        '''"Машина поехала"'''
        self.speed = speed
        return f'{self.name} машина поехала скорость {self.speed}'
        # return "Машина поехала"

    def stop(self):
        '''Машина остановилась'''
        self.speed = 0
        return f'{self.name} машина остановилась'
        # return "Машина остановилась"

    def turn(self, direction):
        '''Машина повернула'''
        if direction not in ('лево', 'право'):
            # print(f"'{direction}' не корректное значение поворота")
            return f"'{direction}' не корректное значение поворота"
        if not self.speed:
            # print(f"'Не возможно повернуть на {direction}' не двигаясь")
            return f"'Не возможно повернуть на {direction}' не двигаясь"
        self._direction = direction
        return f"Машина {self.name} повернула на '{direction}'"
        # return "Машина повернула на " + direction

    def show_speed(self):
        '''Показать текущую скорость'''
        return f'Текущая скорость {self.name} - {self.speed} км/ч'

    def direction(self):
        '''Текущее направление поворота'''
        return self._direction


class TownCar(Car):
    '''Класс городских автомобилей'''
    _max_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name}   {self.speed}')

        if self.speed > self._max_speed:
            return f'Скорость {self.name} слишком большая для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'


class SportCar(Car):
    '''Класс спортивных автомобилей'''

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    '''Класс рабочих автомобилей'''
    _max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего авто {self.name}   {self.speed}')

        if self.speed > self._max_speed:
            return f'Скорость {self.name} слишком большая для рабочего автомобиля'


class PoliceCar(Car):
    '''Класс полицейских машин'''

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не машина полиции'


accord = SportCar(100, 'красный', 'Honda - Accord', False)
uaz = TownCar(30, 'белый', 'УАЗ - Патриот', False)
lada = WorkCar(70, 'черный', 'Лада - Веста', True)
priora = PoliceCar(60, 'синий', 'Лада - Приора', True)


print(lada.turn("лево"))
print(f'Когда {uaz.turn("право")}, затем {accord.stop()}')
print(f'{accord.show_speed()}')
accord.go(30)
print(f'{accord.show_speed()}')
print(f'{lada.go(50)} со {lada.show_speed()}')
print(f'{lada.name} цвета {lada.color}')
print(f'{accord.name} это полицейская машина? {accord.is_police}')
print(f'{priora.name}  Это полицейская машина? {priora.is_police}')
print(f'{uaz.name}  Это полицейская машина? {uaz.is_police}')
print(accord.show_speed())
print(uaz.show_speed())
print(priora.police())
print(priora.show_speed())
