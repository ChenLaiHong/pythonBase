"""
【问题描述】编程求一组数中离平均数最近的那个整数。计算位于前面的部分数的平均值，并返回离该平均值最近的那个数。
【输入形式】输入一行整数；最后一个是参与求平均的数的个数len。例如：1 2 3 4 5 6 7 10 12 13 8；意思是前面有10个数，最后的
8是说前面8个数参与求平均，而不是10个数参与求平均。
【输出形式】离平均数最近的那个数。例如：5
【样例输入】1 2 3 4 5 6 7 10 12 13 8
【样例输出】5
"""
import numpy as np
numList = input().split()
num = int(numList[numList.__len__()-1])
temp = numList[0:num]
while num > 0:
    temp[num-1] = int(numList[num-1])
    num -= 1
# 求平均值
av = np.mean(temp)
temp.append(av)
temp = sorted(temp)
if temp.count(av) == 1:
    if av - temp[temp.index(av)-1] > temp[temp.index(av)+1] - av and temp.index(av) != temp.__len__()-1:
        print(temp[temp.index(av)+1])
    else:
        print(temp[temp.index(av)-1])
else:
    print(av)