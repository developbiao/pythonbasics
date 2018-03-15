#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import time, functools

def metric(func):
    @functools.wraps(func)
    def decorator(*args, **kw):
        begin_time = time.time()
        retval = func(*args, **kw)
        spend_time = (time.time() - begin_time) * 1000
        print('%s executed in %.2f ms' % (func.__name__, spend_time))
        return retval
    return decorator

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

print('Programing is runing!')
