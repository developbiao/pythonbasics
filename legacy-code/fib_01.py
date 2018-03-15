#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

number = input('Please input something:')
number = int(number)
fib(number)

