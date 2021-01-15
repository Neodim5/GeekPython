__author__ = 'Neklyudov Dmitry'
'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, 
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени 
сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса 
Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        '''
        :param name: имя сотрудника
        :param surname: фамилия сотрудника
        :param position: дожность
        :param wage: оклад
        :param bonus: премия
        '''
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        '''
        метод получения полного имени сотрудника
        :return: объединённое имя с фалимлия
        '''
        return self.name + ' ' + self.surname

    def get_total_income(self):
        '''
        метод расчета дохода с учетом премии
        :return:
        '''
        return self._income.get('wage') + self._income.get('bonus')


engener = Position('Ivan', 'Sidorov', 'Engener', 10000, 25000)
print(engener.get_full_name())
print(engener.position)
print(engener.get_total_income())
