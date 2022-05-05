
# 变量
a= 10
print(a)

# python 数值分为三种: 整数,浮点数,复数
# 在Python中所有的整数都是int类型
b = 20
print(b)

#
# python中下划线会被自动忽略
c = 20_20
print(c)

# 二进制,使用0b开头
c = 0b10
print(c)
# 八进制,使用0o开头
c = 0o10
print(c)
# 十六进制,使用0x开头
c = 0x10
print(c)

# 小数都是浮点数
c = 1.23
c = 4.56

c = 0.1 + 0.2
# 0.30000000000000004,浮点数,近似值
print(c)

print('---------------------------字符串--------------------------')
# 字符串使用引号引起来,不区分单双引号(不可混用),相同的引号不可嵌套
# 使用''' 可以保留格式
d = 'admin'
e = '''测试1
测试2
测试3
'''
print(d)
print(e)

# \t : 制表符
# \n : 换行符
# \\ : \
# \uxxxx : 表示Unicode编码

f = '\u0040'
print('f =', f)

# print 多个参数会进行格式化
g = 'abc' + 'def'
print('g =', g)

print('---------------------------占位符--------------------------')

# 占位符, 使用%s来进行占位,%后进行补充,多个参数使用括号包裹
g = 'Hello %s' % '张超超'
print('g =', g)
g = 'Hello %s 你好 %s' % ('张超超', '在做什么')
print('g =', g)

# 占位符,限制长度 %4,最小4位,少了补充空格
# %4.8,最小4位,最多8位

g = 'Hello %4s' % '张超超'
print('g =', g)
g = 'Hello %4.8s' % '张超超我是谁啊啊啊啊啊啊啊'
print('g =', g)

# 占位符 %f,表示浮点数 .2f,最多两位小数

h = 'Hello %2f' % 0.123
print('h =', h)
h = 'Hello %.2f' % 0.123
print('h =', h)
# 占位符 %d,表示整数
i = 'Hello %2d' % 0.123
print('i =', i)
i = 'Hello %.2d'
print('i =', i)


print('---------------------------格式化字符串--------------------------')
# 可以使用变量在引号,使用{},但是必须在字符串前加一个f
jj = '张超超'
j = f'hello {jj}'
print('j =', j)
print(f'j = {j}')


print('---------------------------复制字符串--------------------------')
# 字符串作乘法，会将字符串进行多个复制
k = '张超超'
k = k * 2
print(f'k = {k}')
print('k = %s' % k)
print('k = ' + k)
print('k =', k)

print('---------------------------布尔值（整型）----------------------')
# 布尔值也是整形，True 为 1 False 为 0
k = True
print(k)
k = False
print(k)
print(k + 1)


print('---------------------------类型检查----------------------')

# 使用type函数来进行类型检查
l = 123
m = '123'
print('l =', l, type(l))
print('m =', m, type(m))

print(type(1))
print(type(1.2))
print(type(True))
print(type('hello'))
print(type(None))

print('---------------------------对象----------------------')
# 每个对线要保存三种数据,id, type 一旦确定不可改变,除非对象销毁
# id : 通过id() 函数查看,id是由解析器生成的,在python中,id就是对象的内存地址
# type : 类型,用来表示当前对象所属类型, int, str, float, bool,可以通过type()来查看
# value : 值,
print('id =', id(123))
print('id =', type(123))
print('id =', 123)

# 对象,代表值的可变,不可变
# 可变对象:
# 不可变对象:


print('---------------------------类型转换----------------------')

# 不是改变对象类型,而是创建新的对象,python是强类型的语言,一旦创建不可改变
# 转换为整型
n = True
o = int(n)
print('n =', n)
print('o =', o)
# 转换为浮点型
o = float(n)
print('o =', o)
# 转换为字符串
o = str(o)
print('o =', o)
# 转换为布尔值
o = bool(None)
print('o =', o)


print('---------------------------算数运算符----------------------')

# +
# -
# x
# / 返回浮点数
# // 整除,没有小数点后
# ** 幂运算,求一个值的几次幂
# % 取模,取余数


print('---------------------------赋值运算符----------------------')

# += 给a加5
a = 10
a += 5
# -=
a -= 5
# *=
a *= 5
# **=
a **= 5
# /=
a /= 5
# //=
a //= 5
# %=
a %= 5
print('---------------------------关系运算符----------------------')

# >
# >=
# <
# <=
# ==
# !=

# is 两个对象是否是同一个对象,比较的是对象的id
# is not 和 is 相反

# 两个字符串进行比较,实际比较的是Unicode编码

print('---------------------------逻辑运算符----------------------')

# not 逻辑非,先进行类型转换,然后进行非运算
# and 逻辑与
# or 逻辑或

print('---------------------------非布尔值的与或运算----------------------')

# 将其当作布尔值运算,最终返回原值
# 找False,若第一个值为False,则直接返回
# 若第一个值不是False,则返回第二个值

result = 1 and 2
print('result =', result)

result = 1 and 0
print('result =', result)

result = 0 and 1
print('result =', result)

result = 0 and None
print('result =', result)

# 或运算
# 找True,若第一个值为True,直接返回
# 若第一个值不是,则返回第二个

result = 1 or 2
print('result =', result)

result = 1 or 0
print('result =', result)

result = 0 or 1
print('result =', result)

result = 0 or None
print('result =', result)


print('---------------------------条件运算符----------------------')

# 语句: 语句1 if 条件表达式 else 语句2
# 条件表达式为True时,执行语句1,否则执行语句2

print("我是真的") if False else print("我是假的")

a = 50
b = 40
c = 30

max = a if a > b else b
print("max =", max)


print('---------------------------运算优先级----------------------')

# and 优先级高,先执行and,再执行or
# 优先级可根据运算符表格,越往下,优先级越高
# 可通过加括号,来改变优先级
a = 1 or 2 and 3
print(a)
a = (1 or 2) and 3
print(a)


# 逻辑运算符,是根据中间值来进行比较
result = 1 < 2 < 3
print(result)













