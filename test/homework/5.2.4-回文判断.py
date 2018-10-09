"""
【问题描述】
回文是正读和倒读都一样的句子。读入一个最大长度不超过50个字符的句子，判断其是否是回文。
【输入形式】
输入一个最大长度不超过50个字符的句子
【输出形式】
如果是回文字符串，则输出Yes，否则输出No
【输入样例】
abcba
【输出样例】
Yes
【样例说明】
输入abcba，判断出它是回文
"""
s = input()
length = s.__len__() % 2
temp = s.__len__() // 2
if length == 0:
    last = s[temp:s.__len__()]
    if s[0:temp] == last[::-1]:
        print("Yes")
    else:
        print("No")
else:
    last = s[temp+1:s.__len__()]
    if s[0:temp] == last[::-1]:
        print("Yes")
    else:
        print("No")