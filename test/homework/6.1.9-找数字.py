"""
【问题描述】编写程序实现：对于一个输入的整数n，判断n的各位数中是否包含数字3或4。若包含，则打印true，否则，打印false。
【输入形式】标准输入的一行表示一个整型数值
【输出形式】标准输出的一行表示判断结果；若输入的数值不合法（如：小数等），输出"illegal input"
【样例输入】132
【样例输出】true
【样例说明】132中有数字3，故输出true
"""
n = input()
if n[0] == "-":
    n = n[1:n.__len__()]
if str(n).isdigit():

    if "3" in str(n) or "4" in str(n):
        print("true")
    else:
        print("false")
else:
    print("illegal input")
