"""
【问题描述】
输入一个浮点数矩阵，输出第3行。
【输入形式】
4行3列的浮点数矩阵。每一行内的元素之间用空格分隔。
【输出形式】
输出第3行。每个浮点数保留1位小数点。元素之间用空格分隔。
【样例输入】
2.56 3.78 4.21
2 3 8
3.1 4.222 8.123
-9.0 -111 9.899
【样例输出】
3.1 4.2 8.1
"""
numList = []
result = []

for j in range(4):
    numList = input().split()
    result.append(numList)
temp = result[2]
for n in temp:
    print("%.1f" % float(n), end=" ")