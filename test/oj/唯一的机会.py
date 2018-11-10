"""
每个人都知道所做出的决定会对所得到的结果产生重大影响。一个众所周知的例子是蒙蒂霍尔悖论，它由三个阶段组成，第三阶段，
竞争者给出了最后一张牌，并且根据他的选择，可能会或者可能不会赢得一辆车。
你必须编写一个程序，检查交换两个字母一次，是否会导致全部字母达到有序序列。请考虑以下字符串：
ABCDFGHIEJ
ABCDEFGHJIKLMNO
第一个例子：对于要排序的第一个字母序列，字母位置之间需要进行多次更改才可有序
第二个例子：I和J交换位置就足够了。
你的任务是检查给出的每个序列，是否在两个字母之间进行单次交换以使其有序。
Input
输入由整数N组成，整数N表示测试用例的数量（1 <= N <= 100）。每个测试用例第一行由一个整数M组成，它表示序列的字母数（2 <= M <= 26）
字母始终为大写，并且不在大于M的索引中。例如：如果M为4，则序列中可能字母为：A，B，C或D；他们的排列先后是随机的。
Output
对于每个序列：
如果序列服从所提到的排序规则：程序必须返回一行显示“There are the chance.”
否则：“There are not the chance.”
Sample Input 1
2
4
ABDC
4
ACDB
Sample Output 1
There are the chance.
There aren't the chance.
Sample Input 2
2
10
ABCDFGHIEJ
26
ZBCDEFGHIJKLMNOPQRSTUVWXYA
Sample Output 2
There aren't the chance.
There are the cha
"""
# A65 Z90
def change(nums):
    temp = []
    for i in range(len(nums)):
        temp.append(ord(nums[i]))
    temp1 = sorted(temp.copy())
    flag = 0
    weizhi = []
    if len(set(temp)) == len(temp):
        for i in range(len(temp)):
            if temp[i] != temp1[i]:
                weizhi.append(i)
                flag += 1
        if flag == 2:
            temp[weizhi[1]], temp[weizhi[0]] = temp[weizhi[0]], temp[weizhi[1]]
            if temp == sorted(temp):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

result = []
N = int(input())
while N > 0:
    M = int(input())
    nums = input()
    result.append(change(nums))
    N -= 1
for i in result:
    if i:
        print("There are the chance.")
    else:
        print("There aren't the chance.")