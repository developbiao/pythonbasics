#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def is_palindrome(n):
    x = n
    op_num = 0
    while n:
        op_num = op_num * 10 + n % 10
        n = n//10
    return x == op_num

# Test
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
