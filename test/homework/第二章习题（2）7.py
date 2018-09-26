"""
【问题描述】
从键盘输入两个举重运动员的成绩信息：
   姓名、体重、抓举成绩、挺举成绩
输出获胜运动员的姓名。
总成绩高者获胜（总成绩=抓举成绩+挺举成绩）
总成绩相同时，体重轻者获胜。
【输入形式】姓名1 体重1 抓举成绩1 挺举成绩1  姓名2 体重2 抓举成绩2 挺举成绩2
【输出形式】获胜运动员的姓名
【样例输入】athlete1  78 120 130  athlete2 80 121 128
【样例输出】athlete1
"""
athlete = input().split()
athlete1 = athlete[0: 4]
athlete2 = athlete[4: 8]
score1 = int(athlete1[2])+int(athlete1[3])
score2 = int(athlete2[2])+int(athlete2[3])
if score1 > score2:
    print(athlete1[0])
elif score1 < score2:
    print(athlete2[0])
else:
    if int(athlete1[1]) > int(athlete2[1]):
        print(athlete2[0])
    else:
        print(athlete1[0])