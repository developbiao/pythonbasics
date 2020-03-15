#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        pass

    def get_grade(self):
        if self.__score >= 90:
            return 'A+'
        elif self.__score >= 80:
            return 'B+'
        else:
            return 'F'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score == score
        else:
            raise ValueError('bad socre')


if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 99)
    bart.print_score()
    bart.set_score(72)
    lisa.print_score()
    print(lisa.get_name(), lisa.get_grade())
    print(bart.get_name(), bart.get_grade())
    print("focre get name:", lisa._Student__name)
