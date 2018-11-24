"""
【问题描述】若将某一素数的各位数字的顺序颠倒后得到的数仍是素数，则此素数称为可逆素数。编写一个判断某数是否可逆素数的函数。
在程序中输入一个整数，再调用此函数进行判断
【输入形式】用户在第一行输入一个整数。
【输出形式】程序在下一行输出yes或是no,yes表示此数是可逆素数，no表示不是。用户输入的数必须为正整数。注意：yes或是no全是小写输出。
【样例输入】23
【样例输出】no
【样例说明】用户输入23，23各位数字颠倒之后得到32，23是素数，但32不是素数，所以23不是可逆素数。 
"""
def isPrime(n):
    n = int(n)
    # 质数大于 1
    if n > 1:
        # 查看因子
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False

num = input()
if isPrime(num) and isPrime(num[::-1]):
    print("yes")
else:
    print("no")