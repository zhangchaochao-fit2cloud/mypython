# 文件
print("-" * 10, "文件", "-" * 10)

# I/O操作

# 打开文件
# 读写
# 保存

# 打开
print("-" * 10, "打开", "-" * 10)

# windows 中路径使用/或者\\
file_name = "demo.txt"
# 文件不存在会报错
demo = open(file_name, encoding="utf-8")
print(demo.name)

# 读取文件内容
content = demo.read()
print(content)

# 关闭
demo.close()

print("-" * 10, "with ... as", "-" * 10)
# with ... as 语句,自动会close,

with open(file_name, encoding="utf-8") as file_obj:
    print(file_obj.read())

print("-" * 10, "with ... as配合try", "-" * 10)

try:
    with open(file_name, encoding="utf-8") as file_obj:
        print(file_obj.read())
except FileNotFoundError as e:
    print("文件不存在!", e, type(e))
else:
    print("文件执行成功")
finally:
    print("finally")

print("-" * 10, "读取大文件", "-" * 10)

file_content = ""
try:
    with open(file_name, encoding="utf-8") as file_obj:
        # read 接收参数（字符），每次读取文件长度
        # print(file_obj.read())
        # print(file_obj.read(6))
        chunk = 100
        while True:
            content = file_obj.read(6)

            # 检测是否读取到内容
            if not content:
                break
            # print(content, end="")
            file_content += content
except FileNotFoundError as e:
    print("文件不存在!", e, type(e))
else:
    print("文件执行成功")
finally:
    print("finally")

print(file_content)

print("-" * 10, "readline", "-" * 10)

from pprint import pprint

# 读取一行
with open(file_name, encoding="utf-8") as file_obj:
    print(file_obj.readline())
# 读取多行，存储在列表中
with open(file_name, encoding="utf-8") as file_obj:
    pprint(file_obj.readlines())

print("-" * 10, "写入", "-" * 10)

# 打开文件需要指定操作，默认为读取
# w 文件不存在会创建文件，存在则覆盖文件
#   返回值为写入的字符长度
with open(file_name, encoding="utf-8", mode="w") as file_obj:
    pprint(file_obj.write("write, hello"))
# a 不存在会创建,追加到后面
with open(file_name, encoding="utf-8", mode="a") as file_obj:
    pprint(file_obj.write("\nwrite, hello"))
# x 用来创建新文件,存在则报错

# + 为操作增加功能
# r+: 可读,可写,但不会自动创建,不存在会报错
# w+: 可写,可读
# a+: 可写,可读


print("-" * 10, "二进制文件", "-" * 10)

# t 文本文件
# b 读取二进制文件
# with open("二进制文件", mode="rb") as file_obj:
#     # 读取二进制文件,size以字节为单位
#     # 读取文本文件,size以字符为单位
#     new_name="aaa.jpg"
#     print(file_obj.read(100))
#     with open(new_name, "wb") as new_obj:
#         # 定义每次读取大小
#         chunk = 1024 * 100
#         while True:
#
#             content = file_obj.read(chunk)
#             # 如果读取为空则返回
#             if not content:
#                 break
#             # 新文件写
#             new_obj.write(content)


# 中文三个字节代表一个中文字符

print("-" * 10, "_seek 和tell", "-" * 10)

# with open("mode.txt", mode="rb") as file_obj:
#     print(file_obj.read())
#     # 查看读取的位置
#     print(file_obj.tell())
#     # 修改当前读取位置,参数2 0:从头计算,默认值 1:从当前位置计算 2:从最后位置开始计算
#     print(file_obj.seek(50))
#     # 读取最后1个
#     print(file_obj.seek(-1, 2))
#     # 读取最后10个
#     print(file_obj.seek(-10, 2))

# 使用seek修改读取位置时,若是中文则需要注意不可拆分中文,必须为3的倍数

# 文件操作
import os
from pprint import pprint
print("-" * 10, "os", "-" * 10)

# 获取当前目录结构/
pprint(os.listdir())
# 获取当前所在目录
pprint(os.getcwd())
# 切换目录
os.chdir("..")
# 获取当前所在目录
pprint(os.getcwd())

# 创建目录
os.mkdir("aaa")

# 删除目录
os.rmdir("aaa")

# 创建文件
open("aaa.txt", "w")
# 删除文件
os.remove("aaa.txt")


# 源文件, 目标文件
# 重命名
os.rename("aaa.txt", "bbb.txt")






