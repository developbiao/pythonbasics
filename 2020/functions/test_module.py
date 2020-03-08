#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'a test module'

__author__ = 'Gong Biao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello python again!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print('Too many arguments')

if __name__ == '__main__':
    test()
