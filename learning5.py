# dict
print("-" * 10, "dict 字典", "-" * 10)

# 字典(映射,mapping) 作用和列表类似,存储对象的容器
# 列表 存数数据性能好, 查询数据性能差
# 字典 查询数据性能好,存储数据性能差 key-value 结构
# 语法
# {key:value,key:value}
# 字典的key可以使任意对象
# value 只能是任意的不可变对象(int, str, bool, tuple...)
a = {
    "name": "张超超",
    "age": 18
}

print("a:", a)

# 不存在key，报错
print("a[name]:", a["name"])
print("a[age]:", a["age"])
# 不存在key，返回None
print("name", a.get("name"))
print("age", a.get("age"))

# 设置默认值
print("sex", a.get("sex", "男"))


# 创建出来key,只能是str类型
b = dict(name='张超超', age=18)
print("b", b)

# 可以将双值子序列的序列转换为字典
# 双值序列, 序列中只有两个值 (1,2) ("a",2) 'ab'
# 子序列, 如果序列中的元素也是序列,那么我们就称这个元素为子序列
# [(1,2),(3,4)]
c = dict([(1, 2), (3, 4)])
print("双值子序列:", c)
print("len", len(c))

# 添加/修改
c["name"] = "张超超"
print("双值子序列:", c)

# 存在key，返回(不进行修改操作)， 不存在添加，返回默认值
print("default:", c.setdefault("name", "哈哈哈"))
print("default:", c)
print("default:", c.setdefault("haha", "哈哈哈"))
print("default:", c)
print()


# update 合并，若key相同，会覆盖
d = {'a': 1, 'b': 2, 'c': 3}
e = {'c': 1, 'd': 2, 'e': 3}
d.update(e)
print("d：", d)

print()
# 删除
del d['a']
print("del:", d)
# 删除字典中的一个键值对，一般都会删除最后一个键值对
# 会将删除的键值对，以元组的形式返回
# 若删除的是空字典,报错
d.popitem()
print("popitem:", d)
print("popitem:", d.popitem())

# 删除指定的key-value,会将删除的value 返回
# 若是删除的key,不存在报错,若指定了默认值,返回默认值
print("pop:", d.pop("b"))
print("pop:", d.pop("b", "默认值"))

# clear
print("clear:", d.clear())
print("clear:", d)


print("-" * 10, "dict copy", "-" * 10)
print()
# copy 浅复制,若字典内部存在可变对象,则可变对象不会被复制
b = a.copy()
print("b",  b)

a = {"a": {"name": "张超超"}, "b": "哈哈哈"}
b = a.copy()
print("b:", b)
b['a']['name'] = "哈哈哈"
print("a:", a)

print("-" * 10, "dict 遍历", "-" * 10)

print()
print("keys")
for key in a.keys():
    print(key, a[key])
print()
print("values")
for value in a.values():
    print(value)

# 返回元组
print()
print("items")
for item in a.items():
    print(item)

for k, v in a.items():
    print(k, v)

