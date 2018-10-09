"""
【问题描述】
将n元（n是100的倍数）换成用10元、5元、2元的组合（其中每一面值都可取0），一共有多少种组合？输入n，输出组合数。
【输入形式】
输入钱币总额n
【输出形式】
输出组合数
【样例输入】
100
【样例输出】
66
"""
money = int(input())
sum = 0
for i in range(money//10 + 1):
    for j in range((money-i*10)//5 + 1):
            result = money - i*10 - j*5
            if result % 2 == 0:
                sum += 1

print(sum)

