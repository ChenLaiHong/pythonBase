"""
【描述】
给出三维空间中的n个点（不超过10个）,求出n个点两两之间的距离,并按距离由大到小依次输出两个点的坐标及它们之间的距离。
【输入】
输入包括两行，第一行包含一个整数n表示点的个数，第二行包含每个点的坐标(坐标都是整数)。点的坐标的范围是0到100，
输入数据中不存在坐标相同的点。
【输出】
对于大小为n的输入数据，输出n*(n-1)/2行格式如下的距离信息：
(x1,y1,z1)-(x2,y2,z2)=距离
其中距离保留到数点后面2位。
【样例输入】
4
0 0 0 1 0 0 1 1 0 1 1 1
【样例输出】
(0,0,0)-(1,1,1)=1.73
(0,0,0)-(1,1,0)=1.41
(1,0,0)-(1,1,1)=1.41
(0,0,0)-(1,0,0)=1.00
(1,0,0)-(1,1,0)=1.00
(1,1,0)-(1,1,1)=1.00
【提示】
1. 对于一行输出中的两个点(x1,y1,z1)和(x2,y2,z2)，点(x1,y1,z1)在输入数据中应出现在点(x2,y2,z2)的前面。
比如输入：
2
0 0 0 1 1 1
输出是：
(0,0,0)-(1,1,1)=1.73
但是如果输入：
2
1 1 1 0 0 0
输出应该是：
(1,1,1)-(0,0,0)=1.73
2. 如果有两对点p1,p2和p3,p4的距离相同，则先输出在输入数据中靠前的点对。
比如输入：
3
0 0 0 0 0 1 0 0 2
输出是：
(0,0,0)-(0,0,2)=2.00
(0,0,0)-(0,0,1)=1.00
(0,0,1)-(0,0,2)=1.00
如果输入变成：
3
0 0 2 0 0 1 0 0 0
则输出应该是：
(0,0,2)-(0,0,0)=2.00
(0,0,2)-(0,0,1)=1.00
(0,0,1)-(0,0,0)=1.00
"""
import math
num = int(input())
nums = [int(n) for n in input().split()]
temp = []
result = []
result_dict = {}
flag = 0
while flag < len(nums):
    for i in range(flag, flag+3):
        temp.append(nums[i])
    result.append(tuple(temp))
    temp = []
    flag += 3
for i in range(len(result)):
    first = result[i]
    dict_key1 = "("+str(result[i][0])+","+str(result[i][1])+","+str(result[i][2])+")-"
    for j in range(i+1, len(result)):
        if j < len(result):
            second = result[j]
            dict_key2 = "("+str(result[j][0])+","+str(result[j][1])+","+str(result[j][2])+")"
            result_dict[dict_key1+dict_key2] = math.sqrt((second[0] - first[0])**2+(second[1] - first[1])**2+(second[2] - first[2])**2)
        else:
            break
last = sorted(result_dict.items(), key=lambda n:n[1], reverse=True)
for i in last:
    print("%s=%.2f" % (i[0], i[1]))


