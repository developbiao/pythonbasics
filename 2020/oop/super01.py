#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print("Animal is running!")

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    print(isinstance(cat, Animal))
    print(isinstance(dog, Cat))
