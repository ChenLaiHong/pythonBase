"""
【问题描述】
输入一组整数，输入一个整数v，要求在整数数组中删除全部的整数v（若有的话），然后输出删除后的整数数组。未删除的元素的顺序不
允许改变。
【输入形式】
第一行是用空格分隔的一组整数。
第二行是整数v。
【输出形式】
一行用空格分隔的一组整数。
【样例输入】
1 2 3 2 9
2
【样例输出】
1 3 9
"""
num = input().split()
v = input()
while v in num:
    for n in num:
        if n == v:
            num.remove(v)
            break
for r in num:
    print(r, end=" ")




