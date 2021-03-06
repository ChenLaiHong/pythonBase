"""
【问题描述】编写一个程序，求s=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)。
【输入形式】输入一个正整数n，根据求s公式计算s并输出。
【输出形式】输出的为s的结果。
【样例输入】5
【样例输出】35
【样例说明】用户输入一个正整数，按照公式将输入值赋给n，输出计算后的结果。
"""
n = int(input())
count = 1
s = 0
for i in range(n):
    for j in range(1, count+1):
        s += j
    count += 1
print(s)