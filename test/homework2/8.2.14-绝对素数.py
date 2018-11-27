"""
【问题描述】所谓绝对素数是指具有如下性质的素数：一个素数，当它的各位数字逆序排列，形成的整数仍为素数，这样的数称为绝对素数。
例如，11，79，389是素数，其各位数字对换位置后分别为11，97，983仍为素数，因此这三个素数均为绝对素数。编写函数absolute_prime(x)，
判断一个整数是否为绝对素数，如果x是绝对素数则返回1，否则返回0。编写程序，接收控制台输入的两个整数a，b。
调用absolute_prime函数输出所有a到b之间（包括a和b）的绝对素数
【输入形式】控制台输入两个整数a和b，以空格分隔。
【输出形式】输出有若干行，每行有一个a和b之间的绝对整数。输出各行上的数字不重复，且从小至大依次按序输出。
【样例输入】80 120
【样例输出】
97
101
107
113
【样例说明】输入整数a=80，b=120，要求输出所有[80, 120]之间的绝对素数。有97，101，107，113，按升序分行输出。
"""
def absolute_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return 0
        else:
            return 1
    else:
        return 0

a, b = input().split()
a, b = int(a), int(b)
for i in range(a, b+1):
    temp = str(i)[::-1]
    if absolute_prime(i) == 1 and absolute_prime(int(temp)) == 1:
        print(i)
