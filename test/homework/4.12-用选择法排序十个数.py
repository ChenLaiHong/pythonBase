"""
【问题描述】
用选择法对10个整数进行从小到大的排序。
这里采用的选择法的思路是进行9轮比较和交换：
（1）遍历10个数，选出最小的数，该数和10个数中首位置的数进行交换；
（2）遍历末尾的9个数，选出最小的数，该数和末尾9个数中首位置的数的进行交换；
（3）遍历末尾的8个数，选出最小的数，交换至末尾8个数中首位置，......，依次类推，直至排序完成。
【输入形式】
输入十个整数
【输出形式】
输出9行。
前8行是9轮比较和交换后的整数序列。
第9行是排序后的十个整数。
数之间用空格隔开。
【样例输入】
4 5 3 6 7 2 1 8 10 9
【样例输出】
1 5 3 6 7 2 4 8 10 9 
1 2 3 6 7 5 4 8 10 9 
1 2 3 6 7 5 4 8 10 9 
1 2 3 4 7 5 6 8 10 9 
1 2 3 4 5 7 6 8 10 9 
1 2 3 4 5 6 7 8 10 9 
1 2 3 4 5 6 7 8 10 9 
1 2 3 4 5 6 7 8 10 9 
1 2 3 4 5 6 7 8 9 10 
"""
number = input().split()
for n in range(number.__len__()):
    number[n] = int(number[n])

def findMin(numberList):
    temp = sorted(numberList)
    return temp[0]
numberTemp = number.copy()
for t in range(number.__len__()-1):
    # temp = findMin(numberTemp)
    temp = number.index(findMin(numberTemp))
    # 这样交换不成功
    # number[t], number[number.index(temp)] = number[number.index(temp)], number[t]
    number[t], number[temp] = number[temp], number[t]

    for n in range(number.__len__()):
        print(number[n], end=" ")
    print()
    numberTemp = number[t+1: number.__len__()]
