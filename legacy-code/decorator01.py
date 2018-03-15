#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import functools

# decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s call %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('Notice: execute')
def now():
    print('2017-11-23')

print('current function name %s' % now.__name__)
print('Program runing is ok!')
