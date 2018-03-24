#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import threading

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# create global ThreadLocal对象
local_school = threading.local()

def process_student():
    # get current thread  assoc student
    std = local_school.student
    print('Hello, %s (in %s)' % (std.print_score(), threading.current_thread().name))

def process_thread(std):
    # bind ThreadLocal student:
    local_school.student = std
    process_student()

std_alice = Student('Alice', 82)
std_bob = Student('Alice', 33)

t1 = threading.Thread(target= process_thread, args=(std_alice,), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=(std_bob,), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

