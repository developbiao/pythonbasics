#!/usr/bin/env python3
#-*- coding:utf-8 -*-

try:
    with open('./foo.txt', 'r') as file:
        contents = file.read()
except FileNotFoundError:
    print('File not found! Please check the file and try again.')
except:
    print('An error occurrend while reading the file.')
else:
    print('File contents:', contents)
