print("我是test_module模块")

print("__name__:", __name__)


class Person:
    def __init__(self):
        self.name = "张超超"


def test():
    print("我是test方法")


def test2():
    print("我是test方法")


# 私有属性,通过import * 不会引入_开头的变量
_age = 2

# 测试代码,判断是不是主模块,这样作为模块引入的时候不会执行
if __name__== "__main__":
    test()
    test2()

