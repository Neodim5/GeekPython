__author__ = 'Neklyudov Dmitry'

"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
print("Найдите сумму чисел n + nn + nnn")
number = input("Введите целое положительное число n >>> ")

summ = (int(number) + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))

print("Ответ", summ)
