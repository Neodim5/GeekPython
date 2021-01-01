user = ["John", "Artur", "Kate"]


def say_hello(*user_lst):
    for users in user_lst:
        print(users)

say_hello(*user)
