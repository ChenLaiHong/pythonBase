"""
【问题描述】
对于多个N阶矩阵，依次进行加、减运算。
【输入形式】
从标准输入读取输入。第一行只有一个整数N（1<=N<=10），代表矩阵的阶数。
接下来是一个矩阵，是N行，每行有N个整数（可能是正、负整数），是矩阵的所有元素。
然后一行只含一个字符"+"或"-"，代表加、减操作。
然后用同样的方式输入另一个矩阵。
后续仍然是运算符和矩阵。直至运算符为"#"时停止计算，将结果输出。
【输出形式】
向标准输出打印矩阵的操作结果。输出N行，每行对应矩阵在该行上的所有元素，每一行末均输出一个回车符。
每个元素占5个字符宽度（包括负号），向右对齐，不足部分补以空格。
【输入样例】 
3
1 -2 7
2 8 -5
3 6 9
+
3 5 7
-1 2 6
3 7 10
-
1 -2 7
2 8 -5
3 6 9 
#
【输出样例】
（下图中"#"代表空格）
####3####5####7
###-1####2####6
####3####7###10
"""
def num_sum(temp,num_list,flag):
    result = []
    if flag == "+":
        for i in range(len(temp)):
            result_temp = []
            for j in range(len(temp)):
                result_temp.append(str(int(temp[i][j])+int(num_list[i][j])))
            result.append(result_temp)
    else:
        for i in range(len(temp)):
            result_temp = []
            for j in range(len(temp)):
                result_temp.append(str(int(num_list[i][j])-int(temp[i][j])))
            result.append(result_temp)
    return result

num = int(input())
temp = [[0]*num]*num

flag = "+"
while flag != "#":
    num_list = []
    for i in range(num):
        num_list.append(input().split())
    temp = num_sum(num_list, temp, flag)
    flag = input()
for i in temp:
    for j in i:
        print(j.rjust(5), end="")
    print()

