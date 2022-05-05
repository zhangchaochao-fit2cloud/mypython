# 异常
print("-" * 10, "异常", "-" * 10)

'''
    try:
       代码块(可能出现错误的语句)
    except:
        代码块(出现错误以后的处理方式)
    else:
        代码快(没出错时要执行的语句)
'''
try:
    print("异常开始")
    # 可能出现错误的代码
    print(10 / 0)
except ZeroDivisionError as e:
    # 处理
    print("我要处理错误了", e, type(e))
except Exception as e:
    # Exception 是所有异常的父类
    print("我要处理错误了1")
else:
    print("没有要处理异常")
finally:
    print("我是finally")
print("异常结束")

# 抛出异常 raise
# 异常
print("-" * 10, "抛异常raise", "-" * 10)


# 自定义异常
class MyExcept(Exception):
    pass


def add(a, b):
    # 若有负数，抛异常
    if a < 0 or b < 0:
        raise MyExcept("参数中不可以有负数！")
    r = a + b
    return r


print(add(10, -20))


