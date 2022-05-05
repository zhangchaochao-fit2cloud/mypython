# 递归
print("-" * 10, "递归", "-" * 10)


# 求10的阶乘(10!)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4


def factorial(n) -> int:
    """
    该函数用来求任意数的阶层
    :param n: 要求阶层的数字
    :return:
    """
    result = n
    for i in range(1, n):
        result *= i
    return result


def digui(a):
    if a == 1:
        return 1
    return a * digui(a - 1)


# digui(10)
print("10的阶层", factorial(10))
print("10的阶层", digui(10))

print("-" * 10, "递归2", "-" * 10)


def power(n, i):
    if i == 1:
        return n
    """
    用来为任意的数字做幂运算
    :param n: 幂运算的数字
    :param i: 幂运算的次数
    :return:
    """
    return n * power(n, i - 1)


print("10的5次幂：", power(10, 5))
print("10的5次幂：", 10 ** 5)

print("-" * 10, "递归3", "-" * 10)


def hui_wen(s):
    """
    改函数用来检查指定字符串是否回文字符串，若是返回True，否则返回False
    回文字符串，字符串前后念，都是一样的
    :return:
    """
    #  字符串的长度小于2，则一定是回文
    if len(s) < 2:
        return True
    # 若第一个和最后一个比不相等，则不是回文
    elif s[0] != s[-1]:
        return False
    # 切片，包前不包后
    return hui_wen(s[1: -1])


print(hui_wen("qwertyytrewq"))
print(hui_wen("dasdasdas"))

print("-" * 10, "高阶函数", "-" * 10)
# 接收函数作为参数，或者将函数作为返回值的函数是高阶函数

l = [1, 2, 3, 4, 5, 6, 7]


# 定义一个函数,可以将指定列表中的所有偶数,保存到一个新的列表中返回


def fn2(i):
    if i % 2 == 0:
        return True
    return False


# 大于5
def fn3(i):
    if i > 5:
        return True
    return False


def fn(func, lst):
    """
    可以将指定列表中的所有偶数获取到,并保存到一个新列表返回
    :param lst: 要进行筛选的列表
    :return:
    """

    # 内部函数
    # def fn2(i):
    #     if i % 2 == 0:
    #         return True
    #     return False
    #
    # # 大于5
    # def fn3(i):
    #     if i > 5:
    #         return True
    #     return False

    new_list = []
    for n in lst:
        if func(n):
            new_list.append(n)
    return new_list


# filter 内置函数类似
print(fn(fn2, l))
print(list(filter(fn2, l)))

print("-" * 10, "匿名函数 lambda", "-" * 10)


def fn5(a, b):
    return a + b


print("lambda:", (lambda a, b: a + b)(123, 456))

l1 = lambda a, b: a + b

print("lambda:", l1(123, 456))

# map 添加新对象返回
l = [1, 2, 3, 4, 5, 6]
r = map(lambda a: a + 1, l)
print("r:", list(r))

print("-" * 10, "sort", "-" * 10)

# sort 直接改变值
m = ['a', 'we', 'f', 'ew', 'we']

m.sort()

print(m)

# 根据长度排序
m.sort(key=len)
print(m)

# str,会将转换为str来进行排序
m = [1, 3, 's', 5, 'qwe']
m.sort(key=str)
print(m)

# sorted 返回新值,不会影响源内容
print(sorted(m, key=str))

print("-" * 10, "闭包", "-" * 10)

# 形成闭包的条件
"""
    1.函数嵌套
    2.将内部函数作为返回值返回
    3.内部函数必须要使用到外部函数的变量
"""


# 全局变量 拿不到闭包内的属性值(私有属性)
def make_averager():
    nums = []

    def averager(n):
        nums.append(n)

        # 求平均值
        return sum(nums) / len(nums)

    return averager


averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))

print("-" * 10, "装饰器", "-" * 10)


def add(a, b):
    return a + b


def muli(a, b):
    return a * b


# *p 接收没有关键字的参数
# **kwargs 接收关键字参数
def new_func(func, *p, **kwargs):
    print("程序开始执行~~~~")
    # print(*p)
    # print(*kwargs)
    print(func(*p, **kwargs))
    print("程序执行结束~~~~")


# new_func(add, 10, b=20)
# new_func(add, 10, 20)
# new_func(muli, 10, b=20)
# new_func(muli, 10, 20)


# ---------装饰器模式----------
# 使用注解的方式来进行 使用
def begin_end(old):
    def new_func(*args, **kwargs):
        print("开始执行~~~")
        # 扩展函数
        result = old(*args, **kwargs)
        print("执行结束~~~")
        return result

    return new_func


# 使用了这种方式，函数直接被改变
# 可以使用多个装饰器，与装饰注解的顺序有关
@begin_end
def say_hello():
    print("大家好~~~")


say_hello()


