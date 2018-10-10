"""
例如：输入
2000 1 1
2002 10 1
输出
1004
"""
# 月份是31天的
month = [1, 3, 5, 7, 8, 10, 12]
run = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ping = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first = input().split()
second = input().split()
for i in range(first.__len__()):
    first[i] = int(first[i])
    second[i] = int(second[i])

# 判断是否是闰年
def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
# flag=1时计算某个月份到年尾的天数，否则求某年第一天到某月某日的天数
def temp(timeList, flag):
    result = 0
    day = 365
    if leap(timeList[0]):
        day = 366
    if flag == 1:
        if timeList[1] == 1:
            result = day - timeList[2]
        else:
            for i in range(timeList[1] - 1):
                result += run[i]
            result += timeList[2]
            result = day - result
    else:
        if leap(timeList[0]):
            if timeList[1] == 1:
                result = timeList[2]
            else:
                for i in range(timeList[1] - 1):
                    result += run[i]
                result += timeList[2]
        else:
            if timeList[1] == 1:
                result = timeList[2]
            else:
                for i in range(timeList[1] - 1):
                    result += ping[i]
                result += timeList[2]
    return result

result = 0
for i in range(first[0] + 1, second[0]):
    if leap(i):
        result += 366
    else:
        result += 365
result += temp(first, 1) + temp(second, 0)
print(result)
