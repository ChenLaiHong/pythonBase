"""
【问题描述】输入一个整数k，求1到k以内(不含该整数)能被3整除且个位数为6的所有整数,并输出
【输入形式】一个整数k
【输出形式】一组整数。在一行中从小到大输出，数之间用空格隔开。
【样例输入】7
【样例输出】6
"""

def search(k):
    result = []
    for i in range(k):
        temp = str(i)
        if i % 3 == 0 and int(temp[-1]) == 6:
            result.append(i)
    return result


k = int(input())
result_list = search(k)
for r in result_list:
    print(r, end=' ')