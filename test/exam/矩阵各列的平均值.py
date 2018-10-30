"""
【问题描述】编写程序计算一个5*5的矩阵s中每列的平均值。
【输入形式】标准输入的每一行表示矩阵的一行，以空格作为间隔。
【输出形式】标准输出的一行为各列的平均值，以空格作为间隔。
【样例输入】
            1.0 2.0 3.0 4.0 5.0
            2.0 3.0 4.0 5.0 1.0
            3.0 4.0 5.0 1.0 2.0
            4.0 5.0 1.0 2.0 3.0
            5.0 1.0 2.0 3.0 4.0
【样例输出】3.0 3.0 3.0 3.0 3.0
"""
temp = []
for i in range(5):
    nums = input().split()
    temp.append(nums)
result = []
numSum = 0

for i in range(5):
    for j in temp:
        numSum += float(j[i])
    result.append(numSum/5)
    numSum = 0
for i in result:
    print(i, end=" ")