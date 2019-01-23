"""
给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
一个点的坐标（x，y）由一个有两个整数的整数数组表示。
示例:
输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
"""
import math
def validSquare(p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    result = set()
    temp = [p1, p2, p3, p4]

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            result.add(math.sqrt((temp[j][0]-temp[i][0])**2 + (temp[j][1]-temp[i][1])**2))
    print(result)
    if len(result) == 2 and 0 not in result:
        return True
    else:
        return False
print(validSquare([0,0],[1,1],[0,0],[0,0]))

