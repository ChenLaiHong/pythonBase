"""
【问题描述】统计一行字符的大写字母，小写字母和数字的个数。先输出大写字母个数，在输出小写字母个数，最后输出数字个数。
【输入形式】ljaij1A
【输出形式】
1
5         
1
【提示】用字符串的方法isupper, islower来判别大小写。isdigit来判断是否是数字。
"""
num = input()
isupperNum = 0
islowerNum = 0
isdigitNum = 0
for n in num:
    if n.isupper():
        isupperNum += 1
    elif n.islower():
        islowerNum += 1
    elif n.isdigit():
        isdigitNum += 1
print(isupperNum)
print(islowerNum)
print(isdigitNum)
