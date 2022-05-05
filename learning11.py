# 对象
print("-" * 10, "面向对象", "-" * 10)


# 封装 继承 多态
# 封装确保了数据的安全性
# 使用getter setter

# 隐藏属性
# 使用__开头,对象的隐藏属性,隐藏属性只能在类内部访问,无法通过对象访问
# python 实际上也是将属性名修改了,_类名__属性名 比如: _Person__name

# 私有属性
# 使用_开头,没有特殊需要不要修改私有属性


class Person:

    def __init__(self, name, age):
        # 隐藏属性
        self.__name = name
        # 私有属性
        self._age = name

    def get_name(self):
        return self.__name

    def st_name(self, name):
        self.__name = name


p = Person("张超超", 18)
# 隐藏属性访问
p._Person__name = "测试"
print(p.get_name())

print("-" * 10, "装饰器", "-" * 10)


# getter 和 setter 必须同时存在
class Student:
    def __init__(self, name):
        self._name = name

    # getter装饰器,将一个get方法,转换为对象的属性
    # 可以直接使用属性来进行访问get方法
    @property
    def name(self):
        return self._name

    # setter装饰器
    @name.setter
    def name(self, name):
        self._name = name


s = Student("张超超")
# getter装饰器可以直接使用属性
print("name", s.name)
# 实际调动的setter方法
s.name = "测试"
print("name", s.name)

print("-" * 10, "继承", "-" * 10)


# 默认父类为object，所有类都集成object
class Teacher(Person):
    pass


t = Teacher("张超超", 18)

print("name", t.get_name())

# 集成关系，会将对象变为多个类的实例
print("Teacher", isinstance(t, Teacher))
print("Person", isinstance(t, Person))

# 检查一个类是否是另一个类的子类
print("object", issubclass(Teacher, object))

# 子类会重写父类的属性
# 若需要初始化父类的属性
# 可以在子类中调用父类的初始化方法


print("-" * 10, "继承", "-" * 10)


class Animal:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name


class Gog(Animal):

    # 可以调用父类的init来初始化父类中定义的属性
    # super() 表示父类属性
    # 不允许直接写Animal.__init__(self,name)来初始化父类属性,不灵活
    def __init__(self, name, age):
        super().__init__(name)
        # Animal.__init__(self, name)
        self.age = age

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age


print("-" * 10, "多重继承", "-" * 10)


# 类名.__bases__ 这个属性可以获取当前类的所有父类
# 多重继承,会使子类同时继承多个父类,并且会获取到所有父类的方法

# 应该尽量避免多重继承,会使代码复杂
# 若多个父类中有同名的方法,则会在前面的父类中寻找,覆盖后面的

class A(object):
    def test(self):
        print("AAA")


class B(object):
    def test2(self):
        print("BBB")


class C(A, B):
    def test(self):
        print("CCC")


print("C的父类", C.__bases__)
print("B的父类", B.__bases__)

c = C()

c.test()
c.test2()


# 多态(一个方法只需要确定参数,不需要确定类型)
# len()
# 一个对象通过len()获取长度,因为对象具有特殊方法__len__
# 只需要对象中具有__len__特殊方法,就可以通过len()调用他的长度


# 面向对象三大特征
# 封装
#     确保数据安全
# 继承
#     保证对象可扩展
# 多态
#     保证程序灵活

# 类方法
class A(object):
    # 类属性,直接在类中定义属性
    # 类属性可以通过类或者类的实例访问
    # 但是类属性只能通过类对象来修改,无法通过实例对象修改
    count = 0

    def __init__(self):
        # 实例属性,通过实例对象添加的属性属于实例属性
        # 实例属性只能通过实例对象来访问和修改,类对象无法访问修改
        self.name = "张超超"

    # 实例方法
    # 在类中定义,以self为第一个参数的方法都是实例方法
    # 实例方法在调用时,python会将调用对象作为self传入
    # 实例方法可以通过实例和类调用
    #   通过实例调用,会自动将当前调用对象作为self传入
    #   通过类对象调用,不会自动传递self,此时必须手动调用self
    def test(self):
        print("这是一个测试方法~~~", self)

    # 类方法
    # 在类中使用 @classmethod 来修饰的方法属于类方法
    # 类方法第一个参数是cls,会自动传递,cls就是当前类对象
    # 类方法和实例方法区别,实例方法第一个参数是self,类方法第一个参数是cls
    @classmethod
    def test_2(cls):
        print("这是test_2方法, 它是一个类方法", cls)

    # 静态方法
    # 在类中使用 @staticmethod 来修饰的方法属于静态方法
    # 静态方法不需要指定参数,可以通过类和实例取调用
    # 静态方法基本和当前类无关的方法，只是一个保存到当前类中的函数
    # 一般都是一些工具方法，和当前类无关
    @staticmethod
    def test_3():
        print("test_3执行了")


a = A()

# 实例属性,听过实例对象添加的属性属于实例属性
a.count = 10
A.count = 100

# print("A", A.count)
# print("a", a.count)
# print("A", A.name)
# print("a", a.name)

# a.test() 等价于 A.test(a)

# A.test_2() 等价于 a.test_2()

# A.test_3()
# a.test_3()