#!/usr/bin/env python3
#-*- coding:utf-8 -*-

f = open("./foo.txt", "r")

for line in f:
    print(line, end='')

f.close()

