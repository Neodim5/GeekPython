'''
Первая строка отвечает за импорт списка аргументов командной строки,
переданных скрипту (sys.argv). В следующей — осуществляется распаковка
содержимого списка argv в переменные.

python script_params_test.py раз 2 true

'''
from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Параметр 1: ", first_param)
print("Параметр 2: ", second_param)
print("Параметр 3: ", third_param)
