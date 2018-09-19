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