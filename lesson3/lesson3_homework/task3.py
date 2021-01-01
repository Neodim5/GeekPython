__author__ = 'Neklyudov Dmitry'
'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''


def my_func(arg1, arg2, arg3):
    '''
    принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    возвращает сумму наибольших двух аргументов
    '''

    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

print(F'Решение - {my_func(a, b, c)}')
