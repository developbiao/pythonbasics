#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print("Animal is runing!")

class Pig(Animal):
    def run(self):
        print("Pig is runing!")
    def eat(self):
        print("Eating grass...")

class Dog(Animal):
    def eat(self):
        print("Eating meat...")

class Tortoise(Animal):
    def run(self):
        print("Tortoise is runing slowly...")

# run twice
def run_twice(animal):
    animal.run()
    animal.run()


print("----Animal-----")
animal = Animal()
animal.run()

print("----Pig----")
pig = Pig()
pig.run()
pig.eat()

# check instance
'''
a = list()
b = Animal()
c = Pig()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Pig))
print(isinstance(c, Animal))
'''


print("===== Runing twice =====")
run_twice(Tortoise())


