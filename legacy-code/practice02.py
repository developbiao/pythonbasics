#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import math # this will import math module

height = input('Please input your height:')
weight = input('Please input your weight:')

bmi = float(weight) / math.pow(float(height), 2)

print('You are bmi is :%f' % bmi);

if(bmi > 32):
    print('Very fat!')
elif(bmi >= 28 and bmi < 32):
    print('fat!')
elif(bmi >= 25 and bmi< 28):
    print('some fat~~')
elif(bmi >= 18.5 and bmi < 25):
    print('Nomal')
else:
    print('light');
