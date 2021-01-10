__author__ = 'Neklyudov Dmitry'
'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников 
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить 
подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
'''
import sys

filename = 'task3.txt'
min_salary = 20000
salary = []
poor = []

try:
    with open(filename) as my_file:
        my_list = my_file.readlines()
except IOError as err:
    print(err)
    sys.exit(1)

summ_salary = 0
print('Сотрудники ЗП меньше ', min_salary)
for i in my_list:
    name, sal = i.split()
    try:
        sal = float(sal)
    except ValueError:
        continue
    summ_salary += sal
    if sal < min_salary:
        print(name)
print('Средняя зарплата: ', round(summ_salary/ len(my_list), 2))
