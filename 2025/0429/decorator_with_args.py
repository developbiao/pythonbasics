# -*- encoding: utf-8 -*-

def my_decorator(func):
    def wrapper(arg1, arg2):
        print('Wrapper of decorator')
        func(arg1, arg2)
    return func

@my_decorator
def greet(arg1, arg2):
    print('Hello world')
    print('arg1: {}, arg2: {}'.format(arg1, arg2))

greet('Hello Beijing', 'I from Chengdu')

