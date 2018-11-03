"""
【问题描述】平面上有两个矩形A和B，其位置是任意的。编程求出其相交部分（即重叠部分）的面积。（0<a，b<1000）
【输入文件】从标准输入读取两行以空格分隔的整数，格式如下：
Ax1 Ay1 Ax2 Ay2
Bx1 By1 Bx2 By2
其中（x1，y1）为矩形一个顶点座标，（x2，y2）为前一顶点的对角顶点座标。各座标值均为整数，取值在0至1000之间。
【输出文件】向标准输出打印一个整数，是两矩形相交部分的面积（可能为0）。在输出末尾要有一个回车符。
【输入样例】
0 0 2 2
1 1 3 4
【输出样例】
1
【样例说明】输入的两个矩阵的相交面积为1
"""
Ax1, Ay1, Ax2, Ay2, = input().split()
Bx1, By1, Bx2, By2, = input().split()
A = []
B = []
def find(x1, x2):
    if x1 > x2:
        MAX_AX, MIN_AX = x1, x2
    else:
        MAX_AX, MIN_AX = x2, x1
    return MAX_AX, MIN_AX
Ax = find(Ax1, Ax2)
Bx = find(Bx1, Bx2)
Ay = find(Ay1, Ay2)
By = find(By1, By2)

lessx = int(Ax[0]) if int(Bx[0]) > int(Ax[0]) else int(Bx[0])
morex = int(Bx[1]) if int(Bx[1]) > int(Ax[1]) else int(Ax[1])
lessy = int(Ay[0]) if int(By[0]) > int(Ay[0]) else int(By[0])
morey = int(By[1]) if int(By[1]) > int(Ay[1]) else int(Ay[1])
if lessx - morex >0 and lessy - morey >0:
    print((morex-lessx) * (morey-lessy))
else:
    print(0)