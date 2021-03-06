"""
【问题描述】
输入一个五位数，左对齐依次输出其数位，中间用3个空格间隔。如输入12345，则输出：
1     2     3     4     5
输出以上内容的python语句是
       print (1," ",2," ",3," ","4," ",5)
说明：1之后的逗号,会产生一个空格，加上指定输出的空格和2之前的逗号产生的空格，一共隔了3个空格。
【输入形式】
输入一个5位的整数
【输出形式】
输出各数位，数位之间间隔3个空格。
【样例输入】
12345
【样例输出】
1     2     3     4     5
"""
number = input()
num = 0
for i in number:
    num += 1
    if num < 5:
        print(i, "  ", end="")
    else:
        print(i)