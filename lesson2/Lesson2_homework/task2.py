__author__ = 'Neklyudov Dmitry'
'''
Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''
count_list = int(input("Введите количество элементов списка >>>"))
list_m = []
i = 0
# for i in
while i < count_list:
    list_m.append(input(f"Введите значение списка {(i + 1)} >>>"))
    i += 1
print(list_m)

el = 0
# range(int(len(list_m) / 2))
for index in range(int(len(list_m) / 2)):
    list_m[el], list_m[el + 1] = list_m[el + 1], list_m[el]
    el += 2

print(list_m)
