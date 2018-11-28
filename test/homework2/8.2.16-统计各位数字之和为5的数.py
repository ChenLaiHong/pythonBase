"""
【问题描述】下面的函数count统计m和n（m和n都是3位数）之间（包含m和n本身）有多少个数其各位数字之和是5，并将统计结果 返回。
【输入形式】两个整数 m n
【输出形式】m和n之间各位数字之和为5的所有整数的个数
【样例输入】100 200
【样例输出】5
"""
def count(m, n):
    count_num = 0
    start = min(m,n)
    end = max(m,n)
    for i in range(start, end+1):
        temp = str(i)
        if int(temp[0])+int(temp[1])+int(temp[2]) == 5:
            count_num += 1
    return count_num


m, n = input().split()
m = int(m)
n = int(n)
print(count(m, n))