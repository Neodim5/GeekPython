number = 1


def increment(a):
    """

    :param a:
    :return:
    """
    global result
    print(a)
    result = a + 1
    print(result)


increment(number)
print(number)
print(result)
