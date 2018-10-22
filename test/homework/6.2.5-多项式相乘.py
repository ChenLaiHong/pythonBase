"""
【问题描述】
编写一个程序实现两个一元多项式相乘。
【输入形式】
首先输入第一个多项式中系数不为0的项的系数和指数，以一个空格分隔。且该多项式中各项的系数均为0或正整数，系数和最高幂次不会
超过int类型的表示范围。对于多项式 anxn +a n-1 x n-1 + ...+ a1x1 + a0x0 的输入方法如下：
an  n  a n-1  n-1 ...  a1  1  a0  0 
即相邻两个整数分别表示表达式中一项的系数和指数。在输入中只出现系数不为0的项。最后一项的指数后没有空格，只有一个回车换行符。
按照上述方式再输入第二个多项式。
【输出形式】
将运算结果输出到屏幕。将系数不为0的项按指数从高到低的顺序输出，每次输出其系数和指数，均以一个空格分隔，最后一项的指数后
也可以有一个空格。
【样例输入】
10 80000 2 6000 7 300 5 10 18 0
3 6000 5 20 8 10 6 0
【样例输出】
30 86000 50 80020 80 80010 60 80000 6 12000 21 6300 10 6020 31 6010 66 6000 35 320 56 310 42 300 25 30 130 20 174 10 108 0
【样例说明】
输入的两行分别代表如下表达式：
10x80000 + 2x6000 + 7x300 + 5x10 + 18
3x6000 + 5x20 + 8x10 + 6
相乘结果为：
30x86000 + 50x80020 + 80x80010 + 60x80000 + 6x12000 + 21x6300 + 10x6020 + 31x6010 + 66x6000 + 35x320 + 56x310 + 42x300 
+ 25x30 + 130x20 + 174x10 + 108
"""
first = input().split()
second = input().split()


def find(numList):
    xi = []
    zhi = []
    for i in range(numList.__len__()):
        if i % 2 == 0:
            xi.append(numList[i])
        else:
            zhi.append(numList[i])
    return xi, zhi
firstXi = find(first)[0]
firstZhi = find(first)[1]

secondXi = find(second)[0]
secondZhi = find(second)[1]
result = {}
for i in range(firstXi.__len__()):
    for j in range(secondXi.__len__()):
        zhishu = int(firstZhi[i])+int(secondZhi[j])
        xishu = int(firstXi[i])*int(secondXi[j])
        if zhishu in result:
            result[zhishu] += xishu
        else:
            result[zhishu] = xishu

# 根据字典的键去排序
r = {}
for k in sorted(result.keys(), reverse=True):
    d = {k: result[k]}
    r.update(d)
for i in r:
    print(r[i], i, end=" ")
