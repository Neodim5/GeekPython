__author__ = 'Neklyudov Dmitry'
'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон. 
 Функция должна принимать параметры как именованные аргументы. 
 Реализовать вывод данных о пользователе одной строкой.
'''


def user_print(**user_def) -> None:
    """ Выводит в одну строку данные пользователя
    :param user_data: данные пользователя
    """
    print(f'Имя: {user_def.get("name")}, фамилия: {user_def.get("surname")}, год рождения: {user_def.get("born_y")}, город проживания: {user_def.get("city")}, email: {user_def.get("email")}, телефон: {user_def.get("phone")}')


user = {
    'name': 'Дмитрий',
    'surname': 'Неклюдов',
    'born_y': '1983',
    'city': 'Новосибирск',
    'email': 'mail@ngs.ru',
    'phone': '630559',
}

user_print(**user)
