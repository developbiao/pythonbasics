# -*- coding: utf-8 -*-

height = float(input('Please input your height: '))
weight = float(input('Please input your weight: '))

bmi = weight / height ** 2

# Colorful green
print("Your bmi is \033[32;1m%.2f\033[0m" % bmi)

if bmi < 18.5:
    print('Light')
elif 18.5 < bmi <= 25:
    print('Normal')
elif 25 < bmi <= 28:
    print('Overweight')
elif bmi > 32:
    print('Fat')

