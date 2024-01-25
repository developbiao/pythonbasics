# -*- encoding: utf-8 -*-

import math

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

if __name__ == '__main__':
    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)
