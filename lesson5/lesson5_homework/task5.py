__author__ = 'Neklyudov Dmitry'
'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import sys

filename = 'task5.txt'
try:
    with open(filename, 'w+') as file_obj:
        line = input('Введите целые числа через пробел \n')
        file_obj.writelines(line)
except IOError as err:
    print(err)
    sys.exit(1)
except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')

try:
    with open(filename) as file_obj:
        my_line = file_obj.readline()
        my_line = my_line.split()
        print(sum(map(int, my_line)))
except IOError as err:
    print(err)
    sys.exit(1)