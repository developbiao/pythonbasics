#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('socre must be an integer')
        if value < 0 or value > 100:
            raise ValueError('socre must be between 0 ~ 100')
        self._score = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise  ValueError('name must be a sring')
        if len(value) <= 0:
            raise ValueError('name lenth must be great than 0')
        self._name = value

if __name__ == '__main__':
    s = Student()
    s.score = 100
    print(s.score)
    s.name = ''
    print(s.name)
    # s.score = 3000
    # print(s.score)

