__author__ = 'Neklyudov Dmitry'
'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь 
определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: 
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов 
на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные 
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.
'''


class Textil:
    #    V = int
    #    H = int
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.V = V
        self.sq_coat = round(self.V / 6.5 + 0.5)

    def get_sq_coat(self):
        return f'Площадь ткани на костюм - {self.V / 6.5 + 0.5}'

    def __str__(self):
        return f'Площадь ткани на пальто {self.sq_coat}'


class Jacket(Textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.square_j = round(self.H * 2 + 0.3)

    def get_square_j(self):
        return f'Площадь ткани на костюм - {self.H * 2 + 0.3}'

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_j}'


coat = Coat(3, 2)
jacket = Jacket(2, 4)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(coat.get_sq_coat())
print(jacket.get_square_j())
