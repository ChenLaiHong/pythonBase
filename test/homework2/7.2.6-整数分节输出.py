"""
【问题描述】编写一个程序，将某个位数不确定的正整数进行三位分节后输出。
【输入形式】用户在第一行输入一个正整数。
【输出形式】程序将这个正整数三位分节输出，每隔三位加一个逗号（英文逗号）分割。
【样例输入】1234567
【样例输出】1,234,567
【样例说明】用户输入正整数1234567，程序从个位开始每隔三位加一个逗号（英文逗号）分割，所以输出为1,234,567
"""
num = input()
temp = num[::-1]
result = ""
length = 1
while length < num.__len__()+1:
    result += temp[length-1]
    if length % 3 == 0:
        result += ","
    length += 1
result = result[::-1]
if result[0] == ",":
    print(result[1:])
else:
    print(result)