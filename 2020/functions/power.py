#!/usr/bin/python
# -*- encoding: utf-8 -*-

def power(x, n):
        s = 1
        while n > 0:
            s = s * x
            n -= 1
        return s

print power(5, 3)
