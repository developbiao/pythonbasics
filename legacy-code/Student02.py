#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = score

print('====Start @property test=====')
s1 = Student()
s1.set_score(77)
print(s1.get_score())
