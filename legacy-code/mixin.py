#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Runnable(object):
    def run(self):
        print('Runing...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
        pass
