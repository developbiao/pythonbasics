#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def createCounter():
    def _odd_iter():
        n = 0
        while True:
            n += 1
            yield n
    y = _odd_iter()
    def counter():
        print('--come here--')
        return next(y)
    return counter

c1 = createCounter()
print(c1(), c1(), c1())
print("Program 2 runing is ok\n");

