def print_decorator(func):
    def wraper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wraper


@print_decorator
def show_massage(content):
    print(content)


# show_massage = print_decorator(show_massage)


show_massage('Hello,World')
