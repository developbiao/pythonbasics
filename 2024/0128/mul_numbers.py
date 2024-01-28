# multiply numbers
def mul(x, *args):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be int or float")
    elif args is None:
        return x
    else:
        for i in args:
            if not isinstance(i, (int, float)):
                raise TypeError("args must be int or float")
            x = x * i
        return x


if __name__ == '__main__':
    print(mul(2, 3, 3))
