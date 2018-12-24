"""
Fi二进制数是一个只包含0和1的数字。它不包含任何前导0.并且它不包含2个连续1.
前几个这样的数字是1,10,100,101,1000,1001 ，1010,10000,10001,10010,10100,10101等。给你n。您必须计算第n个 Fi-Binary数字
Input
输入以整数T（≤10000）开始，表示测试用例的数量。每一种情况下包含一个整数N（1≤N≤10 9）。
Output
对于每种情况，请打印案例编号和第n个 Fi-Binary编号
Sample Input 1
4
10
20
30
40
Sample Output 1
Case 1: 10010
Case 2: 101010
Case 3: 1010001
Case 4: 10001001
"""
# 二进制的转换
def Dec2Bin(dec):
    result = ''

    if dec:
        result = Dec2Bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result
print(Dec2Bin(10))
print(Dec2Bin(20))
print(Dec2Bin(30))
print(Dec2Bin(40))
print(Dec2Bin(80))
# T = int(input())
# while T > 0:
#     num = int(input())
#     print()

