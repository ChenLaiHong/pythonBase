"""
Description
 电梯可以在不同的楼层。然后你必须等电梯才能到达你的楼层。假设电梯从任何楼层到其相邻楼层（向上或向下）需要4秒钟。
 打开或关闭电梯门需要3秒钟，您需要5秒钟才能进入或离开电梯。给出您的位置和升降机的位置，您必须计算到达底层（0楼）的时间。
Input
输入以整数T（≤25）开始，表示测试用例的数量。
每个案例包含两个整数。第一个整数表示您的位置（不是0），第二个整数表示电梯的位置。假设该部门有100层
Output
对于每种情况，以秒为单位打印案例编号和计算出的时间。
Sample Input 1
3
1 2
3 10
5 5
Sample Output 1
Case 1: 27
Case 2: 59
Case 3: 39
"""
n = int(input())
result = []
while n > 0:
    result.append(input().split())
    n -= 1

for i in range(result.__len__()):
    if int(result[i][0]) > int(result[i][1]):
        print("Case %d: %s" % (i+1, 19+((int(result[i][0])-int(result[i][1])+int(result[i][0]))*4)))
    else:
        print("Case %d: %s" % (i+1, 19+int(result[i][1])*4))

