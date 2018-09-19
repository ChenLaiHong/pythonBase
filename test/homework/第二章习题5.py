"""
【问题描述】
从键盘输入一串字母，要求全部变换成大写后输出。
【输入形式】
一个字符串
【输出形式】
字母变成大写后的字符串。
【样例输入】
it's me.
【样例输出】
IT'S ME.
【样例说明】
非字母的字符不用转换。
"""
s = input()
for i in s:
    print(i.upper(), end="")
