# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
#

def practice1():
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for q in range(1, 5):
                if (i != j) and (i != q) and (j != q):
                    count += 1
                    print(i, j, q, "count：", count)
                # if i == j == q:
                #     continue
                # if i == j or j == q or i == q:
                #     continue


practice1()
