#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('我会通过实例运行，我的名字是%s' %  self.name)


robot = Student('老王')
robot()
