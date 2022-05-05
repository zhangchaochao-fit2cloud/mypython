
# 唐僧大战白骨精

print("欢迎来到唐僧大战白骨精")
role=int(input("请选择使用哪个身份进行游戏\n1,唐僧\n2,白骨精\n"))

# if isinstance(role,int):
if role == 1:
    print("选择成功，初始战力：2，生命力：2")
elif role == 2:
    print("不要闹，丑八怪，你肯定不要，自动选择唐僧，初始战力：2，生命力：2")
else:
    print("你输入有误，自动分配为唐僧！")
# else:
#     pass


