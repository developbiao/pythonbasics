# -*- encoding: utf-8 -*-

def my_abs(x):
    if not isinstance(x (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


if __name__ == '__main__':
    print(my_abs(-1))
    print(my_abs(1))
    print(my_abs('A')) 