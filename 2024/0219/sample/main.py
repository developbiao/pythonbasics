from package2.package4 import m2


# 入口文件是不支持相对导入的
#from .package2.package4 import m2
# 如果一定要支持，可以上一一级目标使用 python -m sample.main 运行

if __name__ == '__main__':
    print(m2.m)
    print("Running main.py.")

