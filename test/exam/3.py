"""
【问题描述】
编写程序，定义函数avg，求三个数的平均值并输出。
【输入形式】
三个整数
【输出形式】
它们的平均值，保留两位小数。
【样例输入】
2 3 5
【样例输出】
3.33333
"""

def avg(a,b,c):
    he = a + b + c
    return he/3


line = input()
a_str, b_str, c_str = line.split()
a = float(a_str)
b = float(b_str)
c = float(c_str)
print("%.2f" % avg(a, b, c))