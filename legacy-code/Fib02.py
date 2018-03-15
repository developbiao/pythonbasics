class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a,b

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 100000:
            raise StopIteration()
        return self.a

