"""
【问题描述】
编写一个程序用来计算两个日期之间相差的天数。
【输入形式】
输入两个日期，每个日期分占一行，在一行中日期的年、月、日是三个整数，以空格分隔。并假设第二个日期大于或等于第一个日期。
【输出形式】
第二个日期与第一个日期间相差的天数。
【输入样例】
2003 3 25
2003 3 29
【输出样例】
4
"""
ping = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 判断是否是闰年
def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
# 年份相同计算
def same_year(first,second,result):
    for i in range(first[1], second[1]):
        result += ping[i]
    result += second[2]-first[2]
    if leap(first[0]) and first[1] <= 2 and second[1] > 2:
        result += 1
    return result
# 年份不相同计算
def diff_year(first,second):
    result = 0
    temp = [first[0],12,31]
    while second[0] != first[0]:
        result = same_year(first, temp, 0) + 1
        first = [first[0]+1, 1, 1]
    result += same_year(first,second,0)
    return result
first = input().split()
second = input().split()
result = 0
for i in range(first.__len__()):
    first[i] = int(first[i])
    second[i] = int(second[i])
if first != second:
    if first[0] == second[0]:
        result = same_year(first, second,0)
    else:
        result = diff_year(first,second)

print(result)