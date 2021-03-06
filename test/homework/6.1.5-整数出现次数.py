"""
【问题描述】
输入一组无序的整数，编程输出其中出现次数最多的整数及其出现次数。
【输入形式】
先从标准输入读入整数的个数（大于等于1，小于等于100），然后在下一行输入这些整数，各整数之间以一个空格分隔。
【输出形式】
在标准输出上输出出现次数最多的整数及其出现次数，两者以一个空格分隔；若出现次数最多的整数有多个，则按照整数升序分行输出。
【样例输入】
10
0 -50 0 632 5813 -50 9 -50 0 632
【样例输出】
-50 3
0 3
【样例说明】
输入了10个整数，其中出现次数最多的是-50和0，都是出现3次。
"""
num = int(input())
numList = input().split()
numDict = {}
maxNum = 0
for i in range(numList.__len__()):
    if numList[i] not in numDict:
        numDict[numList[i]] = numList.count(numList[i])
        if numList.count(numList[i]) > maxNum:
            maxNum = numList.count(numList[i])

result = []
for i in numDict:
    if numDict[i] == maxNum:
        result.append(int(i))
for i in sorted(result):
    print(i,maxNum)