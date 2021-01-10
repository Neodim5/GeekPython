__author__ = 'Neklyudov Dmitry'
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и 
считывающую построчно данные. При этом английские числительные 
должны заменяться на русские. Новый блок строк должен записываться 
в новый текстовый файл.
'''
import sys

filename = 'task4.txt'
filenameend = 'task4_end.txt'

num_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_file = []
try:
    with open(filename) as file_obj:
        for i in file_obj:
            i = i.split(' ', 1)
            # print(num_rus[i[0]] + i[1])
            new_file.append(num_rus[i[0]] + ' '+ i[1])
        print(new_file)
        file_obj.close()
except IOError as err:
    print(err)
    sys.exit(1)

try:
    with open(filenameend, 'w') as file_obj_2:
        file_obj_2.writelines(new_file)
        file_obj_2.close()

except IOError as err:
    print(err)
    sys.exit(1)
