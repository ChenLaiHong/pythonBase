"""
【问题描述】已知10个四位数输出所有对称数及个数 n，例如1221、2332都是对称数
【输入形式】10个四位数，以空格分隔开
【输出形式】输入的四位数中的所有对称数，对称数个数
【样例输入】1221 2243 2332 1435 1236 5623 4321 4356 6754 3234
【样例输出】1221 2332 2
【样例说明】为测试程序健壮性，输入数中可能包括3位数、5位数等
"""
def find(number):
    temp = 0
    if len(number) == 1:
        return number
    else:
        for n in range(len(number)//2):
            if int(number[n]) == int(number[len(number)-1-n]):
                temp += 1
                continue
        if temp == len(number)//2:
            return number
    return ""
numInput = input().split()
result = []
number = 0
for n in numInput:
    if find(n).__len__() > 0:
        number += 1
        print(find(n), end=" ")
print(number)
