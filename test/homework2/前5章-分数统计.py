"""
【问题描述】
编写程序，输入n个分数(n<=100)，输出最高分、最低分和平均分。
【输入形式】
首先输入整数n，表示输入分数的个数。第二行输入这n个分数。
【输出形式】
输出有三行，从上到小依次为这组数的最高分、最低分和平均分。都保留1位小数。
【样例输入】
3
88 89 90
【样例输出】
90
88
89
"""
num = int(input())
result = input().split()
for i in range(num):
    result[i] = float(result[i])

he = 0
for i in result:
    he += i
print("%.1f" % (max(result)))
print("%.1f" % (min(result)))
print("%.1f" % (he/num))