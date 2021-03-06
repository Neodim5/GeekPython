'''
Программа запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
'''


def my_sum():
    '''
    запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
    :return:
    '''
    sum_res = 0
    end = False
    while end == False:
        number = input('Введите строку чисел, разделенных пробелом или введите х для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'x' or number[el] == 'X' or number[el] == 'х' or number[el] == 'Х':
                end = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Общая конечная сумма {sum_res}')


my_sum()
