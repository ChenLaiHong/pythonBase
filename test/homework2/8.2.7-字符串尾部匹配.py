"""
【问题描述】
编写一函数strend(s, t)，如果字符串t出现在字符串s的尾部，该函数返回1，否则返回0。测试该函数：
先从键盘输入字符串s、t（不超过100个字符），然后调用该函数，并输出返回的结果。
【输入形式】
从键盘分行输入两个字符串：s，t
【输出形式】
输出有两种可能，Yes或No
【输入样例】
abcdefgh
fgh
【输出样例】
Yes
【样例说明】
输入了两个字符串s，t，发现t是在s的尾部，则输出Yes
"""
def strend(s, t):
    start = len(s)-len(t)
    if s[start:len(s)] == t:
        return "Yes"
    else:
        return "No"
s = input()
t = input()
print(strend(s, t))