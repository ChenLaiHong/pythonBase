"""
【问题描述】
输入一组整数，从小到大排序后，输出排序结果。
【输入形式】
一行。一组用空格隔开的整数。
【输出形式】
一行。一组用一个空格隔开的整数，从小到大排列。
【样例输入】
9 8 7 6
【样例输出】
6 7 8 9
【提示】
用列表的sort方法。
"""
num = input().split()
temp = []
for n in num:
    temp.append(int(n))
temp.sort()
for t in temp:
    print(t, end=" ")