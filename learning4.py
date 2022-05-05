# List
print("-" * 10, "List", "-" * 10)

# 列表可以存储多种类型
a = [10, 20, 30, 40, 50]

print(f"我的List {a}")
print(f"我的List {a[3]}")
print(f"我的List长度 {len(a)}")


# 索引为负数，从后往前获取元素，-1为倒数第一个一次类推
print(f"我的List {a[-1]}")

# 切片
print("-" * 10, "List 切片", "-" * 10)
# 切片，分割list，包前不包后（根据索引）
print(f"List {a[1:2]}")
# 从开头截取
print(f"List {a[:2]}")
# 直到最后
print(f"List {a[1:]}")
# 全部， 类似于创建副本
print(f"List {a[:]}")

# 步长，默认1，获取值间隔
print(f"List {a[::3]}")
# 如果步长是负数，从后面开始，像前面取元素
print(f"List {a[::-3]}")


print("-" * 10, "List 通用操作", "-" * 10)

b = [1, 2, 3, 4]
c = [1, 2, 3, 4]
d = b * 2
# list 相加，表示拼接
print("d:", b + c)

# 相乘次数
print("d:", d)

# 检查元素是否存在
print(2 in b)
print(2 not in b)


print("最大值：", max(b))
print("最小值：", min(b))

print("1 的索引：", b.index(1))
print("1 的数量：", d.count(1))



# 序列

print("-" * 10, "序列", "-" * 10)
# 序列是python最基本的一种数据方式
# 数据结构指数据存储的方式
# 序列用于保存一组有序的数据,所有的数据在序列当中都有一个唯一的位置(索引)
#     并且序列中的数据会按照添加的顺序来分配索引
# 序列的分类
'''
序列的分类
可变序列:
    > 列表(list)
不可变序列:
    > 字符串(str)
    > 元组(tuple)
'''

a = [1, 2, 3, 4]

# 修改
a[0] = 5
print(a)

# 删除
del a[0]
print(a)

# 使用切片赋值,可以添加多个元素
a[0:2] = [4, 4, 4]
print(a)

# 使用切片 插入元素
a[0:0] = [0]
print(a)

# 当设置步长时候,序列中的个数必须和切片中的个数一致
a[::2] = [5, 5, 5]
print(a)

# 切片删除
del a[::2]
a[::1] = []
print(a)

# 使用list 将不可变序列变为可变序列
b = "hello"
b = list(b)
print(b)


# 列表的方法
a = [1, 2, 3, 4, 5]

print("a:", a)

# 列表最后添加
a.append(6)
print("append, a：", a)

# 列表,索引处添加，第一个参数为index
a.insert(0, 0)
print("insert, a：", a)

# 清空列表
a.clear()
print("clear, a:", a)

# 合并，必须为列表
a.extend([1])
a += [2]
print("extend, a:", a)

# 删除，索引元素，有返回值,没有索引，默认删除最后一个
a.pop(1)
print("pop, a:", a)

# 删除，删除指定值，若存在多个值，则只删除第一个
a.remove(1)
print("remove", a)

a = [4, 2, 3, 9]
# 反转
a.reverse()
print("reverse, a:", a)
# 排序，默认从小到大
a.sort()
print("sort, a:", a)
# 排序，默认从大到小
a.sort(reverse=True)
print("sort reverse, a:", a)

print("-" * 10, "List 遍历", "-" * 10)

b = [1, 2, 3, 4, 5, 6]

i = 0
while i < 6:
    print(b[i])
    i += 1
print()
i = 0
while i < len(b):
    print(b[i])
    i += 1

print()
for i in b:
    print(i)


print("-" * 10, "range", "-" * 10)

# 用来生成一个自然数的序列
# 参数： 起始序列(省略，默认0)，结束位置，步长(省略，默认1)
c = range(5)
d = range(10, 0, -1)
print("c: ", list(c))
print("d: ", list(d))

# 配合for使用
for i in range(5):
    print(i)


print("-" * 10, "tuple", "-" * 10)
# 不可变序列

# 创建
my_tuple = ()
print("tuple:", my_tuple)

# 不可变，不能重新赋值，进行增删改操作
my_tuple = (1, 2, 3, 4, 5)
print("tuple:", my_tuple)

# 有数据的元组，可以省略括号
my_tuple = 1, 2, 3, 4, 5
print("tuple:", my_tuple)
# 元组里有一个值，需要添加,来区分
my_tuple = 1,
print("tuple:", my_tuple)
print("tuple:", type(my_tuple))


# 元组的解包（解构）
# 将元组的每个元素都赋值给变量
my_tuple = 1, 2, 3, 4
a, b, c, d = my_tuple

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# 可以使用解包，使用*，表示一个数组，只能有一个*
a, b, *c = my_tuple
print("a:", a)
print("b:", b)
print("c:", c)

print("-" * 10, "列表解包", "-" * 10)
# 也可以对列表进行解包
a, b, *c = [1, 2, 3, 4]
print("a:", a)
print("b:", b)
print("c:", c)


print("-" * 10, "字符串解包", "-" * 10)
# 也可以对字符串进行解包
a, b, *c = 'hello'
print("a:", a)
print("b:", b)
print("c:", c)


print("-" * 10, "交换", "-" * 10)
# a b 交换
a = 100
b = 200

a, b = b, a
print("a:", a)
print("b:", b)

print("-" * 10, "可变对象", "-" * 10)

# id, 标识（type）, 值（value）
# 可变对象 value可变

# == 比较的是值是否相等
# is 比较的是对象是否相等（内存地址）



