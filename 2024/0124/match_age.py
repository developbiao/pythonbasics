# -*- coding:utf-8 -*-

age = int(input('Please input your age: ')) 
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')



