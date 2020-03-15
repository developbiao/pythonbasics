#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A+'
        elif self.score >= 80:
            return 'B+'
        else:
            return 'F'

if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 99)
    bart.print_score()
    lisa.print_score()
    print(lisa.name, lisa.get_grade())
    print(bart.name, bart.get_grade())
