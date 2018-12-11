"""
【问题描述】
对于矩阵来说，矩阵乘法具有结合律和分配率，但不具有交换率。（二维数组）然而，对于n*n的两个方阵A, B来说，
可能两者的乘法具有A*B = B*A（其中*为矩阵乘法），我们称这两个方阵关于矩阵乘法具有交换性质。请你编写函数comm，
判定给定的两个4阶方阵（即4X4矩阵）是否具有交换性质。
然后编写程序，输入两个4阶矩阵，判定是否具有交换性质，若是则输出yes，否则输出no。
【输入格式】
一开始有4行，每行有4个整数，用空格分隔，表示矩阵A；
接下来还有4行，每行有4个整数，用空格分隔，表示矩阵B；
【输出格式】
输出只有一行，若输入的两个矩阵具有交换律，输出yes，否则输出no。
样例输入
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
样例输出
yes
"""
def comm(nums1,nums2):
    result = []
    temp = []
    for i in range(len(nums1)):
        for j in range(len(nums1[i])):
            temp.append(nums1[i][j] * nums2[j][i])
        result.append(temp)
        temp = []
    return result

nums1 = []
nums2 = []
n = 4

while n > 0:
    temp = input().split()
    temp = [int(n) for n in temp]
    nums1.append(temp)
    n -= 1
n = 4
while n > 0:
    temp = input().split()
    temp = [int(n) for n in temp]
    nums2.append(temp)
    n -= 1
if comm(nums1,nums2) == comm(nums2,nums1):
    print("yes")
else:
    print("no")
