"""
【问题描述】编写一个程序，输出当前时间的下一秒。
【输入形式】用户在第一行按照小时:分钟:秒的格式输入一个时间。
【输出形式】程序在下一行输出这个时间的下一秒。
【样例输入】23:59:59
【样例输出】0:0:0
【样例说明】用户按照格式输入时间，程序输出此时间的下一秒。
"""
time = input().split(":")
temp = time.copy()
for i in range(time.__len__()):
    time[i] = int(time[i])
    temp[i] = int(temp[i])
n = 2
while n >= 0:
    if temp[2] < 59:
        time[2] += 1
        break
    else:
        if n != 0:
            if temp[n] == 59:
                time[n] = 0
                time[n-1] += 1
        else:
            if time[n] >= 23 and temp[n+1] == 59:
                time[n] = 0

    n -= 1
length = time.__len__()
for i in range(length):
    if i == length-1:
        print(time[i])
    else:
        print(time[i], end=":")


