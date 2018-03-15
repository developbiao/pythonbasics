#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

try:
    print('try...')
    r = 10 / int('2') 
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
