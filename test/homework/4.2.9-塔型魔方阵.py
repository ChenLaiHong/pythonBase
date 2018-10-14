"""
【问题描述】输入一个自然数Ｎ（1<=N<=9），要求输出如下的魔方阵，即边长为2*N-1，Ｎ在中心出现一次，其余位置上的数字
从外向中心逐渐增大。
N=3时：
11111
12221
12321
12221
11111
N=4时：
1111111
1222221
1233321
1234321
1233321
1222221
1111111
【输入形式】从标准输入读取一个整数N。
【输出形式】向标准输出打印结果。输出符合要求的方阵，每个数字占一个字符宽度，在每一行末均输出一个回车符。
【输入样例】3
【输出样例】
11111
12221
12321
12221
11111
【样例说明】输入自然数3，则输出边长为5的方阵，3在方阵的中间出现一次，其余位置上的数字从外向中心逐渐增大。
"""
N = int(input())
temp = []
result = []
for i in range(2*N-1):
    for j in range(2*N-1):
        temp.append(0)
    result.append(temp)
    temp = []
flag = 1
for i in range(N):
    for j in range(i, N*2-(i+1)):
        result[j][i] = result[i][j] = result[j][2*N-2-i] = result[2*N-2-i][j] = flag
    flag += 1

for i in result:
    for j in i:
        print(j, end="")
    print()
