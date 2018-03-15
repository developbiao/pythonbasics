#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.__gender = None

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        if(gender == 'Male' or gender == 'Female'):
            self.__gender = gender
        else:
            prit('please input Male or Female')

    def get_gender(self):
        return self.__gender


    def get_score(self):
        return self.__score

    # set socre method
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print("%s grade is %s:" % (lisa.get_name(), lisa.get_grade()))
lisa.set_score(89)
print("%s current score is %s" % (lisa.get_name(), lisa.get_score()))
print("Force get student name:", lisa._Student__name)
lisa._Student__name = 'New Name' # force set new name

# test set gender and get gender
print("Before gender is :", lisa.get_gender())
lisa.set_gender('Female')
print("After gender is :", lisa.get_gender())

