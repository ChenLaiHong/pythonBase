"""
【问题描述】
输入学生姓名，学号，年龄，数据结构课程成绩，按成绩从小到大排序；成绩相同，按学号从小到大排序。要求使用插入排序来实现。
第1轮插入第1个元素，以后每一轮按输入顺序插入一个元素，输出第1, 2, ..., N轮的插入排序结果。
【输入形式】
第一行是一个整数N（N<1000），表示元素个数；接下来N行每行描述一个元素，姓名都是长度不超过20的字符串，学号，年龄和成绩都是整型。
【输出形式】
输出N行。
第1行是1个元素。
第2行是2个元素按要求排序，按序输出学生学号。学号间隔开一个空格。
第3行是3个元素按要求排序，按序输出学生学号。学号间隔开一个空格。
依次类推。
【样例输入】
3
Alice 10006 18 98
Bob 10002 19 90
Miller 10005 17 92
【样例输出】
10006
10002 10006 
10002 10005 10006 
"""
def numSord(result):
    # 按照指定元素排序
    def getKey(x):
        return x[1]
    def getNum(x):
        return x[0]
    linshi = sorted(result, key=getNum)
    for i in sorted(linshi, key=getKey):
        print(i[0], end=" ")

N = int(input())
temp = []
chengji = []
result = []
while N > 0:
    message = input().split()
    temp.append(message[1])
    temp.append(message[3])
    result.append(tuple(temp))
    numSord(result)
    print()
    temp = []
    N -= 1




