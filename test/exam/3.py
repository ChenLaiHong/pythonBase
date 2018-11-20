"""
【问题描述】
 输入n个非负整数，统计n个数中各个数字(0~9)出现的次数，并按照由多到少的顺序输出。(n<=1000)
【输入格式】
第一行输入正整数n，表示总共有n个数。
接下来的n行为n个非负整数(最大值为2^32-1)。
【输出格式】
输出10行，每行有两个数，第一个是数字(0~9)，第二个是该数字出现的次数,中间用一个空格隔开。
按数字出现次数由高到低排序输出,若数字出现的次数相等，则按数字由小到大输出。
【样例输入】
5
123
31
1767
0
9786
【样例输出】
1 3
7 3
3 2
6 2
0 1
2 1
8 1
9 1
4 0
5 0 
"""
n = int(input())
nums_list = []
while n > 0:
    nums_list.append(input())
    n -= 1
tempDict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in nums_list:
    for j in i:
        if int(j) in tempDict:
            tempDict[int(j)] = tempDict[int(j)] + 1
result = sorted(tempDict.items(), key=lambda n: n[0])
result = sorted(tempDict.items(), key=lambda n: n[1], reverse=True)


for key,value in result:
    print(key,value)