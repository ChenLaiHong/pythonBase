"""
【问题描述】
str1、str2是两个有序字符串（其中字符按ASCII码从小到大排序），将str2合并到字符串str1中，要求合并后的字符串仍是有序的，允许字符重复。
最后输出合并后的结果。
【输入形式】
分两行从键盘输入两个有序字符串（不超过100个字符）
【输出形式】
输出合并后的有序字符串
【输入样例】
aceg
bdfh
【输出样例】
abcdefgh
【样例说明】
输入两个有序字符串aceg和bdfh，输出合并后的有序字符串abcdefgh
【评分标准】
结果完全正确得20分，每个测试点4分。
"""
s1 = input()
s2 = input()
temp = s1 + s2
result = ""
for i in sorted(temp):
    result += i
print(result)