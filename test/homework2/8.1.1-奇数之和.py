"""
【问题描述】
将1～p之间奇数顺序累加存入n中，直到其和首次等于或大于q为止或1～p之间所有奇数参与累加为止。
程序输入p,q的值，输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数（分别占一行）。
【输入形式】
分两行输入p和q的值。
【输出形式】
依次输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数
【样例输入】
1000
4000
【样例输出】
4096
64
127
"""
def oddsum(num1, num2):
    he = 0
    numcount = 0
    odd_max = 1
    for i in range(1, num1+1):
        if i % 2 == 0:
            continue
        else:
            if he >= num2:
                break
            odd_max = odd_max if odd_max > i else i
            he += i
            numcount += 1
    print(he)
    print(numcount)
    print(odd_max)
p = int(input())
q = int(input())
oddsum(p, q)
