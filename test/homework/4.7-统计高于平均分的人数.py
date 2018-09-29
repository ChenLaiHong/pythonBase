"""
【问题描述】从若干学生成绩中统计高于(严格的大于)平均分的人数，用-1做为学生成绩数据的结束标志
【输入形式】一组学生的成绩
【输出形式】高于平均分的学生人数
【样例输入】70 50 80 -1
【样例输出】2
"""
num = input().split()
score = []
number = 0
sum = 0
for n in num:
    if float(n) != -1:
        sum += float(n)
        score.append(float(n))
    else:
        break
if score.__len__() > 0:
    av = sum/score.__len__()
    for n in score:
        if n > av:
            number += 1
    print(number)
else:
    print(0)
