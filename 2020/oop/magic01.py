#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Programer(object):
    def __new__(cls, *args, **kwargs):
        print("call __new__ function")
        print(args)
        return super(Programer, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print("call __init__ function")
        self.name = name
        self.age = age

if __name__ == '__main__':
    programer =  Programer('Albert', 25)

