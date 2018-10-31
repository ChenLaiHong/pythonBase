"""
编写一个程序，从键盘输入一个正整数M（2 < M <1000000），求解并依次输出符合下面条件的最大幂次n以及21 + 22 + 23 + ... + 2n的值：
21 + 22 + 23 + ...+ 2n<M
【输入形式】
输入共1行，为正整数M；
【输出形式】
输出共2行，
1)第1行为符合条件的最大整数n；
2)第2行为21 + 22 + 23 + ...+ 2n的和值。
【样例输入】
5
【样例输出】
1
2
"""
M = int(input())
n = 1
he = 2
result = 0
while True:
    if he < M:
        result = he
        result1 = n
    else:
        break
    n += 1
    he += 2**n

print(result1)
print(result)