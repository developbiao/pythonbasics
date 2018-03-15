#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


print("====== @property @setter birth day test ======")
gongbiao = Student()
gongbiao.birth = 1993
print("This year I %d years old" % gongbiao.age)
