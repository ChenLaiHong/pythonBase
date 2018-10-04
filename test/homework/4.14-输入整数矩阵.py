"""
【问题描述】
输入3X4整数矩阵，输出第2行第2列的元素，第3行第4列的元素。
【输入形式】
3行。每一行有4列，元素之间用空格隔开。
【输出形式】
两行。第一行是第2行第2列的元素值。第二行是第3行第4列的元素值。
【样例输入】
1 2 3 4
5 6 7 8
9 10 11 12
【样例输出】
6
12
"""
numList = []
result = []

for j in range(3):
    numList = input().split()
    result.append(numList)
print(result[1][1])
print(result[2][3])