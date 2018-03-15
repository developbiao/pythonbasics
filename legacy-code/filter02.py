#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def not_empty(s):
    return s and s.strip()

data_list = list(filter(not_empty, ['A', '', 'B', None, 'C', '    ']))
print(data_list)
