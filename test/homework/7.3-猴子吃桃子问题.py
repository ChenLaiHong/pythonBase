"""
【问题描述】猴子吃桃问题：
猴子摘下若干个桃子，第一天吃了桃子的一半多一个，以后每天吃了前一天剩下的一半多一个，到第n天吃以前发现只剩下一个桃子，
编写程序实现：据输入的天数计算并输出猴子共摘了几个桃子
【输入形式】输入的一行为一个非负整数，表示一共吃的天数。
【输出形式】输出的一行为一个非负整数，表示共摘了几个桃子，若输入的数据不合法（如：负数或小数），则输出"illegal data"。
【样例输入】3
【样例输出】10
【样例输入2】0
【样例输出2】0

n = 1
for i in range(5, 0, -1):
    n = (n+1) * 2
print(n)
"""
num = input()
n = 1
if float(num) < 0 or num.count('.') == 1:
    print("illegal data")
else:
    number = int(num)
    if number == 0:
        print(0)
    else:
        while number > 1:
            n = (n+1) * 2
            number -= 1
        print(n)