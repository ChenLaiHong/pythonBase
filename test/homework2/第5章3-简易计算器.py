"""
【问题描述】  
编程实现简易的计算器：读入两个整数运算数(data1和data2)及一个运算符(op)，计算表达式data1 op data2的值，
其中op可以是+,-,*,/。
【输入形式】
控制台输入运算数和运算符:
1.首先输入以空格分隔的两个整数，分别是data1和data2；
2.输入一个字符作为运算符op，op可以是+, -, *, /。
输入时，data1、data2、op之间各留有一个空格。具体格式见样例输入。
【输出形式】
控制台输出运算结果。作除法运算时，若能够整除，则输出为整数，否则输出结果小数点后应保留两位有效数字。
【样例输入】
23 5 *
【样例输出】
115
【样例说明】
输入中先后输入第一个运算数23,第二个运算数5,运算符*,要求对23和5进行乘法运算。计算结果为115。
"""
data1, data2, op = input().split()
data1, data2 = int(data1), int(data2)
if op == "+":
    print(data1+data2)
elif op == "-":
    print(data1-data2)
elif op == "*":
    print(data1*data2)
else:
    if data1/data2 >= 0:
        print(data1//data2)
    else:
        print("%.2f" % (data1/data2))
