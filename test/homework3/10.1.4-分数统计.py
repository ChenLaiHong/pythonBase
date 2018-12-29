"""
【问题描述】
从一个文本文件内读入任意多个学生的分数，求出最高分，最低分和平均分存入文件result.txt内。
【输入形式】
一个文件，文件中分数之间由换行隔开，输入的文件名为grade.txt。输入的分数都是整数。
【输出形式】
计算出grade.txt中所有分数的最高分，最低分和平均分并分3行存入result.txt的文件内。平均分保留1位小数。
【样例输入】
60
70
80
【样例输出】
80
60
70
【样例说明】
输出的70是平均分。
"""
r = open("grade.txt")
f1 = open("result.txt", "w")
# 读写操作
content = r.readlines()
temp = []
for i in content:
    temp.append(i.strip())
# 关闭文件
r.close()
temp = [int(n) for n in temp]
f1.write(str(max(temp)) + "\n")
f1.write(str(min(temp)) + "\n")
f1.write(str("%0.1f" % (sum(temp)/len(temp))) + "\n")
f1.close()