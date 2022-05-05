from time import *


# 循环语句
print("========== 循环语句 ==========")
print("hello\n" * 4)
num = 1
while num <= 4 :
    print("我是：", num)
    if num == 2:
        break
    num += 1

a = 0
result = 0
while a < 100:
    if a % 2 == 1:
        result += a
    a += 1
    print(a)
print(result)

start=time()
# 9 9 乘法表
i = 1
j = 1
while i < 10:
    while j < (i + 1):
        print("%s * %s = %s" %(j, i, (i * j)), end='  ')
        j += 1
    else:
        print("行循环结束")
    print()
    i += 1
    j = 1
else:
    # 先占用位置
    pass
sleep(5)
end=time()
print("代码执行时间：", end - start, "秒")
