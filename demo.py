def func():
    def inner():
        pass
    return inner

def func1():
    def wrapper():
        pass
    return wrapper
