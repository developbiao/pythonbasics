#!/usr/bin/env python3
#-*- coding: utf-8 -*-

fpath = r'./py_with.txt';
with open(fpath, 'r') as f:
    s = f.readlines()
with open(fpath, 'w') as w:
    for i in s:
        w.write(i.replace('hello', 'nihao'))
print("Python runing is very well!")
