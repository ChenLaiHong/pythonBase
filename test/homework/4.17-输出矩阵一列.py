"""
【问题描述】
输入一个浮点数矩阵，输出第1列。
【输入形式】
4行3列的浮点数矩阵。每一行内的元素之间用空格分隔。
【输出形式】
输出第1列。每行一个元素。每个浮点数保留1位小数点。元素之间用空格分隔。
【样例输入】
2.56 3.78 4.21
2 3 8
3.1 4.222 8.123
-9.0 -111 9.899
【样例输出】
2.6
2.0
3.1
-9.0
"""
numList = []
result = []

for j in range(4):
    numList = input().split()
    result.append(numList)

for n in range(4):
    if len(result[n][0]) > 2:
        print("%.1f" % float(result[n][0]+"1"))
    else:
        print("%.1f" % float(result[n][0]))