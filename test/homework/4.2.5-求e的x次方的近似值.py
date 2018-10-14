"""
【问题描述】
已知ex的近似值可由下面公式计算得出：
ex=1 + x/1! + x2/2! + x3/3! + ...... + xn/n!
给定x和n，利用上述公式求得ex的近似值。
【输入形式】
从控制台输入小数x，和整数n（n>=1），用空格隔开。
【输出形式】
向控制台输出求得的ex 的近似值（小数点后保留6位有效数据）。
【样例输入】
7   27
【样例输出】
1096.633156
【样例说明】
输入的x为7，n的值为27，即：求e7的近似值，利用上述公式求得的近似值为：1096.633156。
"""
def jiecheng(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i*jiecheng(i-1)

x, n = input().split()
x = float(x)
n = int(n)
result = 1
while n > 0:
    result += x**n/jiecheng(n)
    n -= 1
print("%.6f" % result)