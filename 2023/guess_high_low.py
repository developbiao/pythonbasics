#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

number = 18
guess = -1

print("Guess number game!")

while guess != number: 
	guess = int(input("Please Input guess number:"))
	if guess == number:
		print("Yes Correct!")
	elif guess < number:
		print("To low...")
	elif guess > number:
		print("To hight...")


print("Hello Guess number")

