"""
【问题描述】编写程序对标准输入的10个整数置倒序排列.并输出。
【输入形式】标准输入的前十行代表参与计算的十个整数。
【输出形式】标准输出的一行表示倒序后的数组，以空格作为间隔。
【样例输入】
1
2
3
4
5
6
7
8
9
10
【样例输出】
10 9 8 7 6 5 4 3 2 1
"""
i = 0
num = []
while i < 10:
    num.append(input())
    num[i] = int(num[i])
    i += 1
num.sort(reverse=True)
for n in num:
    print(n, end=" ")