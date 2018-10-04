"""
【问题描述】
编写程序，完成3*４矩阵和4*３整数矩阵的乘法，输出结果矩阵。
【输入形式】
以先行后列顺序输入第一个矩阵，而后输入第二个矩阵。
【输出形式】
先行后列顺序输出结果矩阵，每个元素的显示宽度为8格，屏幕一行只显示矩阵的一行。
例如要计算如下两个矩阵
第一个矩阵    1 2 3 4
              5 6 7 8
              9 1 2 3
第二个矩阵    9 8 7
              6 5 4
              3 2 1
              1 2 3
输入与输出格式如下
【样例输入】
1 2 3 4 5 6 7 8 9 1 2 3 9 8 7 6 5 4 3 2 1 1 2 3
【样例输出】
      34      32      30
     110     100     90
      96       87      78
"""
numList = input().split()
# 存储第一个矩阵
num1 = []
# 存储第二个矩阵
num2 = []
# 临时列表，放到矩阵当做行
temp = []
for n in range(12):
    if (n+1) % 4 != 0:
        temp.append(numList[n])
    else:
        temp.append(numList[n])
        num1.append(temp)
        temp = []
# print(num1)
for n in range(12, 24):
    if (n+1) % 3 != 0:
        temp.append(numList[n])
    else:
        temp.append(numList[n])
        num2.append(temp)
        temp = []
# print(num2)
result = []

for i in range(3):
    sum = []
    for j in range(3):
        s = int(num1[i][0])*int(num2[0][j]) + int(num1[i][1])*int(num2[1][j]) + int(num1[i][2])*int(num2[2][j]) + int(num1[i][3])*int(num2[3][j])
        sum.append(s)
    result.append(sum)
for n in range(3):
    print(str(result[n][0]).rjust(8)+str(result[n][1]).rjust(8)+str(result[n][2]).rjust(8))
