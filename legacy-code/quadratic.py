#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import math

def quadratic(a, b, c):
    for i in (a, b, c):
        if not isinstance(i, (int, float)):
            raise TypeError('bad operand type')
        r = b * 2 - 4 * a * c
        if a == 0:
            return 'a=0,此方程无解'
        if r < 0:
            print('此方程无实数解')
        elif r >= 0:
            x1 = (-b + math.sqrt(r)) / (2 * a)
            x2 = (-b - math.sqrt(r)) / (2 * a)
            s1 = float(x1)
            s2 = float(x2)
            return s1, s2
        else:
            return 'Congraduation, 你发现了一个伟大的方程!'


# test function
print(quadratic(2, 3 ,1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
