print("========== 流程控制语句 ==========")

# 条件判断语句
print("========== 1.条件判断语句 ==========")
a = 50
b = 60
if a < b: print("a比b小")

# 代码块,以缩进开始,直到缩进结束,缩进使用4个空格或者tab键
if a > b:
    print("我是True")
else:
    print("我是False")

# 判断条件根据中间的值进行判断
num = 6
if 10 < num < 20:
    print("num 比10大 比20小")
if 10 < num and num < 20:
    print("num 比10大 比20小")
else:
    print("你猜我是多大")

print("========== 2.函数 ==========")
# 获取用户输入,类似于java的scanner,shell的read,返回值是一个字符串
name = input("请输入名称:")
print("name =", name)

# 按回车键退出
input("请按回车键退出...")

print("\n")
# 练习 if else
age = int(input("请输入你的年龄:\n"))

if age >= 18:
    print("你已经成年了~~~")
else:
    print("小弟弟,你还是个未成年...")


# if elif else
age = int(input("请输入你的年龄:\n"))
if 50 > age >= 18:
    print("你已经是个大人了...")
elif age < 18:
    print("你还说是个弟弟...")
else:
    print("老爷爷就不要在这儿秀了,好吧!!!")

# 练习
# 编写一个程序,获取用户输入的整数,通过程序显示这个数是奇数还是偶数
number = int(input("请输入一个数:\n"))
if (number % 2) == 0:
    print("你是一个偶数哦！")
else:
    print("你是一个奇数哈呀")
# 检查任意一个年份，是否是闰年，若一个年份可以被4整除，不能被100整除，或者可以被400整除，这个年份就是闰年
year = 3000
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("今年是闰年哦")
else:
    print("今年不是润年啊")

# 狗5岁了，相当于人多少岁l,pkl,
# 狗的前两年相当于人的10.5岁，每增加一年增加4岁
# 拿5岁的狗相当于人类年龄的10.5+10.5+4+4+4 = 33
dogAge=int(input("你家的狗狗多少岁呀\n"))
if dogAge <= 0:
    print("不要闹了好不好")
else:
    if dogAge <= 2:
        print("狗狗岁数是：%d" % (dogAge * 10.5))
    else:
        num = dogAge - 2
        # %d整数
        age = "%d" % ((num * 4) + (10.5 * 2))
        print("狗狗的岁数是：", age)

print("哈哈")

