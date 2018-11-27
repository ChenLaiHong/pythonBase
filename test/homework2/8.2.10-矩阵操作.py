"""
【问题描述】输入一个N阶矩阵（3<N<10且N为奇数），矩阵中元素均为整数，取值在-1000至+1000之间。将该矩阵中元素的最大值放在矩阵中心，
元素的最小值放在矩阵的四个边界上，其余位置换成原矩阵中所有元素的和。
【输入文件】从标准输入读取输入。第一行只有一个整数N，代表矩阵的阶数。
后续有N行输入，每行有N个以若干空格分隔的整数，代表矩阵在该行上的所有元素。
【输出文件】向标准输出打印矩阵的操作结果。输出N行，每行对应矩阵在该行上的所有元素，每一行末均输出一个回车符。
每个元素占5个字符宽度（包括负号），向右对齐，不足部分补以空格。
【输入样例】 （下例中#代表空格）
5
7##-1##0##8##9
12#13#14#15#16
-5##-6#-7#-8#-9
21#22#31#33#50
-51#-4#5#11#17
【输出样例】
##-51##-51##-51##-51##-51
##-51##193##193##193##-51
##-51##193###50##193##-51
##-51##193##193##193##-51
##-51##-51##-51##-51##-51
【样例说明】输入矩阵中的最小值为-51，最大值为50，分别放在新矩阵的四个边界和中心，其余位置为原矩阵所有元素的和。
"""
def find(result_list, big, small, sum_nums):
    for i in range(len(result_list)):
        for j in range(len(result_list[0])):
            if i == 0 or i == len(result_list)-1 or j == 0 or j == len(result_list[0])-1:
                result_list[i][j] = small
            elif i == len(result_list)//2 and j == len(result_list)//2:
                result_list[i][j] = big
            else:
                result_list[i][j] = sum_nums

num = int(input())
result = []
big = -1001
small = 1001
sum_nums = 0
while num > 0:
    temp = [int(n) for n in input().split()]
    big = big if big > max(temp) else max(temp)
    small = small if small < min(temp) else min(temp)
    sum_nums += sum(temp)
    result.append(temp)
    num -= 1

find(result,big, small,sum_nums)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(str(result[i][j]).rjust(5), end="")
    print()