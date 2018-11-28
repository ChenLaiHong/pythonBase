"""
【问题描述】编写函数delch(src, ch)，去掉字符串src中的字符ch，并返回新得到的字符串。
【输入形式】一个字符串（不含空格）和要去掉的字符。字符串和字符中间有一个空格。
【输出形式】去掉特定字符后的新字符串
【样例输入】abdsag d
【样例输出】absag
"""
def delch(src, ch):
    while True:
        num = src.find(ch)
        if num != -1:
            src = src.replace(ch, " ")
        else:
            break
    return src.replace(" ","")


src, ch = input().split()
print(delch(src, ch))