"""
【问题描述】
输入n的值和n个数，进行排序并输出。
【输入形式】
首先输入整数个数n；
接着输入n个整数
【输出形式】
从小到大地输出n个整数
 【输入示例】
3
1  5 -10
【输出示例】
-10 1 5
"""
num = int(input())
number = input().split()

while num > 0:
    num -= 1
    number[num] = int(number[num])
number.sort()
for n in number:
    print(n, end=" ")