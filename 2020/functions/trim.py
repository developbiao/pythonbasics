#!/usr/bin/python3
# -*- coding: utf-8 -*-

def trim(s):
    a = " "
    while a in s[:1]:
        s = s[1:]
    while a in s[-1:]:
        s = s[:-1]
    return s

if trim('hello ') != 'hello':
        print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
