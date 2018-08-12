#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time, threading

# suppose this is your balance
balance = 0

def change_it(n):
    # first save last consume, result should be 0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join
t2.join
print(balance)
