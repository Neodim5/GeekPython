__author__ = 'Neklyudov Dmitry'
'''
Создать программно файл в текстовом формате, записать в него построчно данные, 
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

while True:
    str_usr = input("Enter anything: ")
    if str_usr == '':
        exit()
    else:
        with open("task1.txt", "a") as f_obj:
            if f_obj.writable():
                print(str_usr, file=f_obj)
            else:
                print("cant write")
            f_obj.close()
