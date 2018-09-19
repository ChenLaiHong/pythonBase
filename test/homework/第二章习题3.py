""" 	
【问题描述】
输入一串字符，变成首字母大写后输出。
【输入形式】
一串字符，可能包含非字母字符。
【输出形式】
首字母大写后的字符串。
【样例输入】
Glad to meet you.
【样例输出】
Glad To Meet You.
【提示】
输入字符串，不要提供输入提示。下面是示例：
  s = input()
输入的字符串存入变量s。"""
# # capitalize()返回首字母大写后的新字符串，并不会改变字符串本身
# print(name.capitalize())
#
# # title()返回每个单词首字母大写后的新字符串，不会改变本身
# print(name.title())
s = input()
temp = 1
for i in s:
    if i == " ":
        temp = 1
        print(i, end="")
    else:
        if temp == 1:
            print(i.upper(), end="")
            temp = 0
        else:
            print(i, end="")