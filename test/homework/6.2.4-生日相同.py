"""
【描述】
在一个有180人的大班级中，存在两个人生日相同的概率非常大，现给出每个学生的名字，出生月日。试找出所有生日相同的学生。
【输入】
第一行为整数n，表示有n个学生，n<=180。此后每行包含一个字符串和两个整数，分别表示学生的名字（名字第一个字母大写，其余小写，
不含空格，且长度小于20）和出生月(1<=m<= 12)日(1 <=d<=31)。名字、月、日之间用一个空格分隔
【输出】
每组生日相同的学生，输出一行，其中前两个数字表示月和日，后面跟着所有在当天出生的学生的名字，数字、名字之间都用一个空格分隔。
对所有的输出，要求按日期从前到后的顺序输出。 对生日相同的名字，按名字从短到长按序输出，长度相同的按字典序输出。
如果没有任何生日相同的学生，输出：None  。
【样例输入】
6
Avril 3 2
Candy 4 5
Tim 3 2
Sufia 4 5
Lagrange 4 5
Bill 3 2
【样例输出】
3 2 Tim Bill Avril
4 5 Candy Sufia Lagrange
【样例说明】
样例输出中，3月2日有Tim, Bill, Avril三个人在当日出生。
"""
import datetime
# 排序时间
def sortDate(strTime):
    temp = sorted(strTime)
    result = []
    for i in temp:
        mouth = datetime.datetime.strftime(i, "%m")
        print(mouth)
        day = datetime.datetime.strftime(i, "%d")
        if mouth[0] == '0':
            mouth = mouth[1]
        if day[0] == '0':
            day = day[1]
        result.append(mouth+" "+day)
    return result

# 名字长度排序
def nameLen(name):
    return len(name)

num = int(input())
result = {}
strTimeList = []
strTimeSet = set()
name = []
# 把信息放到字典中，时间放到列表里面
for i in range(num):
    temp = input().split(" ", 1)
    result[temp[0]] = temp[1]
    strTimeList.append(datetime.datetime.strptime(temp[1], "%m %d"))


# 找出出现两次及以上的生日
for i in strTimeList:
    if strTimeList.count(i) >= 2:
        strTimeSet.add(i)

if strTimeSet.__len__() > 0:
    finalTime = sortDate(list(strTimeSet))
    print(finalTime)
    for i in finalTime:
        for j in result.items():
            if j[1] == i:
                name.append(j[0])
        print(i, end=" ")
        name = sorted(name, key=nameLen)
        for k in name:
            print(k, end=" ")
        name = []
        print()
else:
    print("None")





