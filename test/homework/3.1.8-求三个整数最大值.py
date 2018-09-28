"""
【问题描述】输入3个整数，输出其中最大的一个 。
【样例输入】1 2 3
【样例输出】3
"""
num = input().split()
temp = int(num[0])
for n in num:
    if int(n) > temp:
        temp = int(n)
print(temp)