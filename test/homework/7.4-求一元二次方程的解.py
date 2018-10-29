"""
【问题描述】一元二次方程：ax2+bx+c=0 （a ╪ 0）
【输入形式】输入a、b和c的值（有理数）
【输出形式】输出x的两个值，或者No（即没有有理数的解）
【样例输入】1 2.5 3
【样例输出】No
【样例输入】1 -2 1
【样例输出】1.00 1.00
【样例输出说明】输出的两个解保留两位小数，大的在前。
"""
import math
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
temp = b**2 - 4*a*c
result = []
if temp < 0:
    print("No")
else:
    result.append(((-1)*b+math.sqrt(temp))/2*a)
    result.append(((-1)*b-math.sqrt(temp))/2*a)
for n in result:
    print("%.2f" % n, end=" ")

