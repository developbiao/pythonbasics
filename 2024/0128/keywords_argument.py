def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


if __name__ == '__main__':
    person('Michael', 30)
    person('Bob', 35, city='Chengdu')
    person('Biao', 29, city='Yaan', job = 'Enginner')

    # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
    extra = {'city': 'ChangSha', 'job': 'PHP Engineer'}
    person('Jun', 23, **extra)

