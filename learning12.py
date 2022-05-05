# 垃圾回收
print("-" * 10, "垃圾回收", "-" * 10)


# 垃圾回收就是将垃圾对象从内存中删除
# python会自动将垃圾回收，不需要手动处理


class A(object):
    def __init__(self):
        self.name = "哈哈哈"

    # del特殊方法，会在对象被垃圾回收前调用
    def __del__(self):
        print("A()对象被删除了")
        pass


a = A()

print(a.name)

# 将a设置成了None，此时没有任何变量对A()进行引用，就成为了垃圾
# 会调用类的__del__方法
a = None

# input("回车键退出...")


print("-" * 10, "特殊方法(魔术方法)", "-" * 10)


# __开头,结尾
# 特殊方法不需要手动调用,特殊方法自动执行

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person name:{self.name}, age: {self.age}"

    # 特殊方法,当前对象使用repr函数时,调用
    # 对象在交互模式时，直接输出的效果
    def __repr__(self):
        return "hello"

    # 小于
    def __lt__(self, other):
        pass

    # 小于等于
    def __le__(self, other):
        pass

    # 等于
    def __eq__(self, other):
        pass

    # 不等于
    def __ne__(self, other):
        pass

    # 大于
    def __gt__(self, other):
        pass

    # 大于等于
    def __ge__(self, other):
        pass

    # 长度
    def __len__(self):
        pass

    # 转换为bool值
    def __bool__(self):
        pass


p1 = Person("张超超1", 18)
p2 = Person("张超超2", 18)

# 当我们打印对象时,实际上打印的是对象的特殊方法__str__的返回值
print(p1)
print(p2)
print(repr(p1))
