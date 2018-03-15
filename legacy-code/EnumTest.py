#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Fmale = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# Test
lilei = Student('lilei', Gender.Male)
hanmeimei = Student('hanmeimei', Gender.Fmale)
if lilei.gender == Gender.Male and hanmeimei.gender == Gender.Fmale:
    print('CongratulationTest Pass!')
else:
    print('Test Failed!')
    
