def person(name, age, *args, city, job):
    print(name, age, args, city, job)


if __name__ == '__main__':
    #person('WangYang', 21, city='Chengdu', job='Teacher')
    person('Jack', 33, 'Beijing', 'Engineer')

