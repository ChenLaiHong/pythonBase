"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。
示例:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
"""
def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    temp = []
    for i in matrix:
        for j in i:
            temp.append(j)
    temp = sorted(temp)
    return temp[k-1]

matrix = [
             [ 1,  5,  9],
             [10, 11, 13],
             [12, 13, 15]
         ]
k = 8
print(kthSmallest(matrix, k))