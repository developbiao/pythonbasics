#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time, threading

# 新线程执行的代码
def loop():
    print('thread %s is runing...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is runing...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='MyLoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
