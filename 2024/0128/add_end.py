# -*- encoding: utf-8 -*-

# 注意： 定义默认参数要牢记一点： 默认参数必须指向不变对象！
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L




if __name__ == '__main__':
    print(add_end())
    print(add_end())

