# 对象
print("-" * 10, "对象", "-" * 10)

# 对象是内存中专门用来存放数据的一块区域
# 对象中可以存放各种数据
# 对象由三部分组成
# 1.对象标识（id）
# 2.对象的类型（type）
# 3.对象的值（value）

# 类
# 首字母大写
# 语法
'''
    class 类名([父类]):
        代码块
'''


class Student:
    # 公共属性,所有对象都可访问
    name = "zcc"

    # 方法,默认会传递一个参数, 创建方法时,默认必须添加一个形参
    def say(self):
        print("你好!", self.name)


class Teacher:
    pass


s = Student()
s2 = Student()

s.name = "张超超"
s.age = 18
s.sex = "男"
print(s.say())
print(s2.name)

# 用来检查一个对象是否是一个对象的实例
print("s: ", isinstance(s, Student))

print("-" * 10, "特殊方法", "-" * 10)


class Person:
    # name = "zcc"

    # 类中可以定义一些特殊方法(魔术方法),特殊方法都是以__开头,__结尾
    # 特殊方法,会在特定的时候自动调用
    def __init__(self):
        print("hello1:")

    #  可重复,但是后面的会覆盖前面的方法(不论参数多少个,都以后面这个为主)
    def __init__(self, name):
        print("hello2:", name)


# 创建对象流程
'''
    1.创建一个变量
    2.在内存中创建一个新对象
    3.类中代码块
    4.__init__(self)执行,对象创建以后立即执行(该方法中的变量,在实例对象中,而普通代码块中的变量,则是在类对象中)
        类似于Java的构造器
    5.将对象的id赋值给变量
'''
p = Person("张超超")

# 手动调用会执行两次
# 一般不需要自己手动调用
# p.__init__()


# 类的基本结构
'''
    class 类名([父类]):
        公共属性。。。
        
        # 对象初始化方法
        def __init__(self, ...):
            pass
        
        
        # 其他方法
        def method_1(self, ...):
            pass
            
            
        def method_2(self, ...):
            pass
'''

print("-" * 10, "类", "-" * 10)


class Dog:

    def __init__(self, name, age, sex, height):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

    def run(self):
        print(f"{self.name} 快乐的奔跑")

    def jiao(self):
        print(f"{self.name} 汪汪汪~~~")

    def chi(self):
        print(f"{self.name} 在偷吃好吃的")


d = Dog("旺财", 4, "母", 100)

d.run()
d.jiao()
d.chi()
