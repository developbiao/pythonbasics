#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class people:
    # Public property
    name = ''
    age = 0
    # Prive property
    __weight = 0

    # Construct
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    # Sepak
    def speak(self):
        print("Hello My name is %s, Im %d years old." % (self.name, self.age))


# inherit
class student(people):
    grade = ''
    def __init__(self, name, age, weight, grade=''):
        # call parent construct
        people.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("Hello My name is %s, Im %d years old, Im a student my grade %s" % (self.name, self.age, self.grade))

# New Instance
xiaoming = people('xiaoming', 27, 70)
xiaoming.speak()

# New student
xiaohua = student('xiaohua', 17, 90, 'Level 3')
xiaohua.speak()

