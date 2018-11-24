"""
【问题描述】
     一个数如果恰好等于它的因子（不含数本身）之和，这个数就称为完数。例如，6的因子1, 2, 3，因此6是完数。
     编程找出1000内的所有完数，按以下格式输出因子：6,factor:1,2,3
 【输入形式】
 无，即不输入任何数值
 【输出形式】
 输出1000内的所有完数。格式为如问题描述。其中每一行输出一个完数。
 【样例输入】
无，即不输入任何数值
提示：采用穷举法来找出一个数n的因子，也就是让a从1一直轮到n-1（此即穷举），如果n整除a，则a为n的因子。
这一做法的改进举措是让a从1轮到n的平方根。
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

n = 6
flag = ""
while n < 1000:
    temp = allFactor(n)
    if n == sum(temp):
        print("%s,factor:" % n, end="")
        for i in temp:
            flag += str(i) + ","
        print(flag[0:len(flag)-1])
    n += 1
    flag = ""