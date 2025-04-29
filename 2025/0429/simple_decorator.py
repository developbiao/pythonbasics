# -*- encoding: utf-8 -*-

def my_decorator(func):
    def wrapper():
        print("Wrapper of decorator")
        func()
    return wrapper

def greet():
    print('Hello world')

# greent = my_decorator(greet)
# greet()

@my_decorator
def greet():
    print("Hello Beijing City!")

greet()
