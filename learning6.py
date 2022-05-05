# set
print("-" * 10, "set 集合", "-" * 10)
'''
集合和列表相似
1.集合中只能存储不可变对象
2.集合中存储的对象是无序的
3.集合中没有重复的元素
'''

a = {1, 2, 3, 4, 5, 1}

print("a:", a)
#空集合
b = set()
print("b:", b)
b = set([1, 2, 3, 4, 5])
print("b:", b)

# 操作set只有转换为list
print("set转list", list(b)[0])

# 使用 in, not in检查集合中的元素
# len 获取集合长度

print("-" * 10, "set add", "-" * 10)
# add添加元素
b.add("6")
print("add,b:", b)

# 无序的, 且相同的不会再次添加
c = set('hello')
c.update(b)
print("c:", c)
# 元组也可以添加
c.update((10, 20, 30, 40))
print("c:", c)
# 字典,只会添加key
c.update({"name": "张超超", "age": 18})
print("c:", c)


print("-" * 10, "set del", "-" * 10)

# 随机删除
#c.pop()
#print("c:", c)
# 删除指定元素
c.remove("name")
print("c:", c)

# clear
c.clear()
print("c:", c)

# copy
print("c:", c.copy())




print("-" * 20, "set 运算", "-" * 20)

s = {1, 2, 3, 4, 5}
d = {7, 4, 6, 2, 5}

# 交集运算
print("交集:", s & d)
# 并集运算
print("并集:", s | d)
# 差集运算,s没有与d交集的值
print("差集:", s - d)
# 差集运算,d没有与s交集的值
print("差集:", d - s)
# 亦或集, 不存在交集的所有值
print("亦或集:", d ^ s)


# 检查一个集合是否是另一个集合的子集(若一个集合中的所有元素都在另一个集合中,则这个集合是另一个集合的子集,而另一个是这个集合的超集)
a = {1, 2, 3, 4}
b = {2, 3}

print("子集", a >= b)
print("超集", b <= a)

print("真子集", a > b)
print("真超集", b < a)





