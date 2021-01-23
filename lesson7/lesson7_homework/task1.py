__author__ = 'Neklyudov Dmitry'
'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора 
класса (метод init()), который должен принимать данные (список списков) 
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных 
в виде прямоугольной схемы.

Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в 
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения 
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть 
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент 
первой строки первой матрицы складываем с первым элементом первой строки 
второй матрицы и т.д
'''

from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        mtrx_rows = len(self.__matrix)
        self.__mtrx_size = frozenset([(mtrx_rows, len(row)) for row in self.__matrix])

        if len(self.__mtrx_size) != 1:
            raise ValueError("Не правильный размер матрицы")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"не поддерживаемый тип объекта")
        if self.__mtrx_size != other.__mtrx_size:
            raise ValueError(f"Размеры матриц различаются")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


mtrx1 = Matrix([[31, 22], [37, 43]])
print(mtrx1, '\n')

mtrx2 = Matrix([[3, 5], [2, 4]])
print(mtrx2, '\n')

print(mtrx1 + mtrx2)
