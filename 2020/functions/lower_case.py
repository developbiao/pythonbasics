#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = list()

for item in L1:
    if isinstance(item, str) == True:
        L2.append(item.lower())

print(L2)

