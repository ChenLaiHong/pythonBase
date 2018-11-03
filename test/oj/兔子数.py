"""
第一个月一对兔子，第三个月长大，此后每个月生出一对兔子。
生出的兔子也三个月长大，长大后每个月生出一对兔子，问你个月后，总共有多少对兔子？
输入
在键盘上输入n（4~20之间），代表总共多少个月。
输出
输出一个整数，代表有多少对兔子。
例：
输入：4    输出：3
输入：5    输出：5
"""
n = int(input())
youzai = 2
chengnian = 0
temp = 1
while temp <= n:
    if temp % 3 == 0:
        chengnian += youzai
        youzai = 0
    else:
        youzai += chengnian*2
    temp += 1
print((youzai+chengnian)//2)