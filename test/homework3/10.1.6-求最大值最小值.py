"""
【问题描述】
从in.txt文件读数据，对于该文件每一行：
    求该行中各个数（可能是整数，也可能是浮点数）的最大、最小值，
    把最大值和最小值写入文件out.txt，写成一行，最大值在前，两个数之间隔两个空格。
30 300 30 201 0 395 92 
353 50  50  202  0 430 100 
35 35  0  50 20  20 430 100 
35 35 1.2 50  20 20 365 85 
32.5   32.5  0 47.5  200  381.33333 89 
【样例输出】
395  0
430  0
430  0
365  1.2
381.33333  0
"""
r = open("in.txt", "r")
f1 = open("out.txt", "w")
# 读写操作
content = r.readlines()
result = []
for i in content:
    result.append(i.split())
# 关闭文件
r.close()
temp = []
for i in result:
    for j in i:
        if "." in j:
            temp.append(float(j))
        else:
            temp.append(int(j))
    f1.write(str(max(temp))+"  " + str(min(temp)) + '\n')
    temp = []
f1.close()