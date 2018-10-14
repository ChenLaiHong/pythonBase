"""
【问题描述】矩阵A，B，规模都为4*4。A的第一行全为1，第二行全为2，第三行全为3，第四行全为4，B的第一行全为4，第二行全为3，
第三行全为2，第四行全为1。求A*B
【输入形式】无。
【输出形式】输出四行。每一行对应结果矩阵的一行。行内元素之间用１个空格隔开。
"""
A = []
B = []
tempA = []
tempB = []
for i in range(4):
    for j in range(4):
        tempA.append(i+1)
        tempB.append(4-i)
    A.append(tempA)
    B.append(tempB)
    tempA = []
    tempB = []
result = 0
for i in A:
    for j in i:
        print((i[0]*B[0][0]+i[0]*B[1][0]+i[0]*B[2][0]+i[0]*B[3][0]), end=" ")
    print()


