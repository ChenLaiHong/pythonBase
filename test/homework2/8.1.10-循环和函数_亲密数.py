"""
【问题描述】
 求整数n以内（含n）的全部亲密数。
说明：如果正整数A的全部因子(包括1，不包括A本身)之和
等于B；且正整数B的全部因子(包括1，不包括B本身)
之和等于A，则将正整数A和B称为亲密数。
1不和其他数形成亲密数。
【输入形式】
输入整数n
【输出形式】
 每一行输出一对亲密数，中间用一个空格隔开。
 每一对亲密数只输出一次，小的在前。
 各对亲密数按序排序，按亲密数中小的那个数从小到大排序。
【样例输入】
3000
【样例输出】
220 284
1184 1210
2620 2924
"""

def allFactor(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    rlist = []
    i = 1
    while i < n:
        if n % i == 0:
            rlist.append(i)
        i += 1
    return rlist

num = int(input())
result = []
"""
说明：如果正整数A的全部因子(包括1，不包括A本身)之和
等于B；且正整数B的全部因子(包括1，不包括B本身)
之和等于A，则将正整数A和B称为亲密数。
"""
while num > 0:
    temp1 = sum(allFactor(num))
    temp2 = sum(allFactor(temp1))
    if num == temp2:
        if temp1 not in result and num not in result and temp1 != num:
            result.append(num)
            result.append(temp1)
    num -= 1

flag = 0
for i in sorted(result):
    if flag != 2:
        print(i, end=" ")
        flag += 1
    if flag == 2:
        print()
        flag = 0


