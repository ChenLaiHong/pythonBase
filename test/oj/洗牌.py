"""
Description
一个卡片包含偶数2n张卡片: a1，a2，.... ，a2n，（a1 <a2 <···<a2n）。卡片最初是排序好的，
卡片中的第一张卡是a1，第二张是a2，依此类推，包中的最后一张卡是a2n。
然后，处理程序重复执行洗牌。洗牌包括两个步骤：
    1、把牌从中间分开两半;
    2、然后将两半中的卡片交错插入。如果步骤1开始时的原始序列是X1，X2，... ，X2n，
    然后在步骤2结束时，卡片序列变为X n + 1，X 1，X n + 2，X 2，.... ，X 2n，X n。
给定卡片中的卡数，编写程序以确定：必须执行洗牌过程的次数，以便卡片再次排好序。
Input
输入包含几个测试用例。测试用例有一个偶整数P（2 ≤ P ≤ 2x 10的5次方），其中P是卡片的数量总和。（跟上面提到的2n 一致)
Output
对于输入中的每个测试用例，程序必须生成一行，包含一个整数，必须执行洗牌过程的最小次数，以便再次对排好序。
Sample Input 1
6
Sample Output 1
3
Sample Input 2
10
Sample Output 2
10
"""
def change(first, second):
    temp = []
    for i in range(first.__len__()):
        temp.append(second[i])
        temp.append(first[i])
    return temp

P = int(input())
result = []

for i in range(1, P+1):
    result.append(i)

weizhi = P // 2
number = 0
temp = result.copy()
while True:
    number += 1
    temp = change(temp[0:weizhi], temp[weizhi:P])
    if temp == result:
        break
print(number)
