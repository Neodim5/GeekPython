__author__ = 'Neklyudov Dmitry'
'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, 
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
from time import sleep


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 10}
    _status = None

    def running(self):
        for color, timer in self.__color.items():
            self._status = color

            print(f"Светофор включен на {self._status}")

            sleep(timer)


TrafficLight = TrafficLight()
TrafficLight.running()

