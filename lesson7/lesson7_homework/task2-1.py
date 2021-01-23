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


class Coat():
    def __init__(self, v):
        # super().__init__(V, H)
        # self.v = v
        self.sq = round(v / 6.5 + 0.5)


class Jacket():
    def __init__(self, h):
        # super().__init__(V, h)
        # self.h = h
        self.sq = round(h * 2 + 0.3)


class Textil:
    def __init__(self):
        self.coat_jacket = []
        self.sq = 0
        self._v: int
        self._h: int

    #    @property
    def add_coat(self, ver):
        #self._v = v
        self.coat_jacket.append(Coat(ver))

    #    @property
    def add_jacket(self, h):
        # self.h = h
        self.coat_jacket.append(Jacket(h))

    def all_sq_textill(self):
        main_sq = self.sq
        for el in self.coat_jacket:
            main_sq += el.square
        return main_sq


#coat = Coat(3)
#jacket = Jacket(2)

text = Textil
text.add_coat(2)
print(text.all_sq_textill)
# text.add_jacket(2)
# text.add_coat(5)
# text.add_jacket(8)
# coat = Coat(3)
# jacket = Jacket(2)
# print(coat)
# print(jacket)
# print(coat.sq_coat)
# print(jacket.get_sq_full)
# print(coat.get_sq_coat())
# print(jacket.get_square_j())
