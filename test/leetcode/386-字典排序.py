"""
给定一个整数 n, 返回从 1 到 n 的字典顺序。
例如，
给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
"""
def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    temp = []
    result = []
    for i in range(1,n+1):
        temp.append(str(i))
    for i in sorted(temp):
        result.append(int(i))
    return result

n = 13
print(lexicalOrder(n))