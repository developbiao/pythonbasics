#!/usr/bin/evn python3
#-*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

list_data = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(list_data)
