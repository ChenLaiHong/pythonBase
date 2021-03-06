"""
【问题描述】
编写程序，输入实数x，通过调用库函数求x的绝对值的平方根的自然对数(log)
【输入形式】
输入一个实数。
【输出形式】
输出计算后的结果。保留5位小数。
【样例输入】
-9
【样例输出】
1.09861
"""
import math

num = float(input())
result = math.log(math.sqrt(abs(num)))
print('%0.5f' % (result))
