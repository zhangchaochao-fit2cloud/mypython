# 模块
print("-" * 10, "模块", "-" * 10)

# 将一个程序分解为一个小的模块
# 通过将模块租户，来搭建一个完整的程序

# 引入模块,多此引入只会实例化一次
# 可以通过test来启用别名
import test_module as test

# __main__ 主模块,一个程序只会有一个
print(__name__)
p1 = test.Person()
print("person.name", p1.name)

# 只引入部分,部分引入的可以直接写类名,不需要携带模块
from test_module import Person, test

# 引入所有内容
# from test_module import *

p = Person()
print("p.name", p.name)
# 部分引入直接使用
test()

# 包
print("-" * 10, "包", "-" * 10)

from module import a

print(a)

# python会将编译过一次的包缓存下来,__pycache__

# 标准库
print("-" * 10, "标准库", "-" * 10)

# python的标准库,可以直接使用
# sys模块: 变量和函数,可以获取到python解析器的嘻嘻
#     或者通过函数来操作Python解析器

# 引入sys
import sys
import os
from pprint import pprint

print(sys)
# 获取执行py文件的参数
print(sys.argv)

# 获取所有模块
print(sys.modules)

# pprint 模块pprin函数提供了格式化
pprint(sys.modules)


# 获取模块的搜索路径(找寻模块的路径)
print(sys.path)

# 运行平台 win32
print(sys.platform)

# 结束程序
# sys.exit("程序结束~~~")

# os模块(操作系统)

print(os)
# 系统变量
print(os.environ['path'])

# 执行操作系统命令
os.system("dir")

