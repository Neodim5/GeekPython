__author__ = 'Neklyudov Dmitry'

"""
 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
number = input("Введите число мин 2 знака: ")
step = 0
for i in number:
    while int(i) > step:
        step = int(i)
print(f"Самое большая цифра в числе {number} >>> ", step)
