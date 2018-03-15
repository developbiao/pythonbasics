#!/usr/bin/env python3

# err_reaise.py

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / 0

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()
