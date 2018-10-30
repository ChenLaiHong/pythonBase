"""
【问题描述】编写一个程序：将输入的一个N进制整数转换成M进制数（N和M在2到16进制之间），
            要求：N进制数和M进制数均以字符串方式存储。
【输入形式】输入的第一行、第二行分别表示N和M的值，第三行表示需要转换的数值k。
【输出形式】输出的一行为k转换后的结果（超过10的数值依次用大写字母ABCDEF表示，A表示10， B表示11，依次类推），
若输入的进制数值不合法（如：N和M没有落在2到16之间，或数据含有指定进制的非法字符（如：N=2时，k为12）），输出"illegal input"。
【样例输入】
2
16
11000011
【样例输出】
C3
"""
N = input()
M = input()
k = input()
result = []
shuzi = [10, 11, 12, 13, 14, 15]
zimu = ["A", "B", "C", "D", "E", "F"]
if not 2 <= int(N) <= 16 or not 2 <= int(M) <= 16 or N in k:
    print("illegal input")
else:
    temp = int(k, int(N))
    result.append(temp % int(M))
    while temp != 0:
        temp = temp // int(M)
        result.append(temp % int(M))

fianl = ''
for i in result[:-1]:
    if i > 9:
        fianl += str(zimu[shuzi.index(i)])
    else:
        fianl += str(i)
print(fianl[::-1])
