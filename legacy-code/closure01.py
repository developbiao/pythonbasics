#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

# this function result always is 9 because return function quote variable i but it not immediately execute 
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

