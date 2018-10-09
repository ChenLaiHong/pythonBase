"""
【问题描述】编写一个程序，用户输入出生日期和当前日期，计算出实际年龄。
【输入形式】用户在第一行输入出生日期，在第二行输入当前日期。日期格式为年.月.日，即中间用.分割。
【输出形式】程序在下一行输出实际年龄。
【样例输入】
1964.2.19
2001.7.21  
【样例输出】37
【样例说明】用户第一次输入的日期为出生日期，回车表示本次输入结束。第二次输入的为当前日期，回车表示本次输入结束。系统返回实际年龄
"""
bir = input().split(".")
now = input().split(".")
for i in range(bir.__len__()):
    bir[i] = int(bir[i])
    now[i] = int(now[i])
if bir[1] > now[1]:
    print(now[0] - bir[0]-1)
elif bir[1] == now[1]:
        if bir[2] > now[2]:
            print(now[0] - bir[0] - 1)
        else:
            print(now[0] - bir[0])
else:
    print(now[0] - bir[0])