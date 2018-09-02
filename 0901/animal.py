#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is runing...')


class Dog(Animal):
    def run(self):
        print('Dog is runing...')

class Cat(Animal):
    def run(self):
        print('Cat is runing...')


dog = Dog()
dog.run()

cat =Cat()
cat.run()
