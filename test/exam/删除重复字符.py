"""
【问题描述】删除字符串中的重复字符
【输入形式】输入一个字符串，全为字母字符
【输出形式】输出删除重复字符后的字符串
【样例输入】abbcbd
【样例输出】abcd
【样例说明】删除第二个和第三个b，保留第一个遇到的不同字符。
"""
words = list(input())
temp = {}
for i in words:
    temp[i] = words.count(i)
for i in temp:
    print(i, end="")
