# help
print("-" * 10, "help", "-" * 10)


# 文档字符串 doc str
# 定义函数时,可以在函数内部编写文档内部字符串,文档字符串就是函数的说明


# 形参类型,只用于文档查看,没有实际用处
# -> 表示返回值类型,也只是描述(编辑器会自动提示,类型对其)
def test1(a: int, b: bool, c: str) -> int:
    """
    文档字符串描述实例
    :param a: 参数
    :param b: 参数
    :param c: 参数
    :return: test
    """
    return 10


a = (10, 20, 30)

result = test1(*a)

print("result:", result)

# 查看文档字符串
help(test1)

print("-" * 10, "namespace 命名空间", "-" * 10)

# 指变量存储的位置,每个变量都需要存储到指定的命名空间中
# 每个作用域都会有一个对应的命名空间
# 全局命名空间,用来保存全局变量,函数命名空间用来保存函数中的变量
# 命名空间实际就是一个字典,用来专门存储变量的字典

# locals() 用来获取当前作用域的命名空间
# 如果全局作用域中调用locals则获取全局命名空间
# 函数作用域中调用locals获取函数命名空间

scope= locals()

# 全局命名空间
print("namespace:", scope)
a = 20
print("namespace a:", scope['a'])

# 直接在namespace 操作
scope['c'] = 30
print("scope c:", c)

# global
# 在函数中获取全局命名空间,需要使用global()


