#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def createCounter():
    counter = 0 
    def bar():
        nonlocal counter
        counter += 1
        return counter
        
    return bar

c1 = createCounter()
print(c1())
print(c1())
print(c1())
print("Program runing is ok\n");

