#/usr/bin/env python3
#-*- coding: utf-8 -*-

' my first python module '

__author__ = 'Gong Biao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello this is my first python module!')
    elif len(args) == 2:
        print("Hello, %s module test success!" % args[1])
    else:
        print("Too many arguments!")
        print(args)

if __name__ == '__main__':
    test()

