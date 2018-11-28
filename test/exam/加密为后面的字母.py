"""
【问题描述】
请编写一加密函数encrypt (info)
该函数对字符串info的加密规律是：对字符串的每个字母以该字母后面第4个字母加以替换。例如，字母'A'后面第4个字母是'E'，
用'E'代替'A'，因此，"China"应译为"Glmre"。
（注意大小写。W变A，X变B，以此类推）
【输入形式】 
字符串
【输出形式】
加密后的字符串
【样例输入】
China
【样例输出】
Glmre
"""
def encrypt (info):
    result = ""
    for i in info:
        if i.isupper():
            temp = ord(i)+4
            if temp > 90:
                temp = temp - 26
            result += chr(temp)
        else:
            temp = ord(i)+4
            if temp > 122:
                temp = temp - 26
            result += chr(temp)
    return result

s = input()
print(encrypt(s))