"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5
"""
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    result = []
    for i in nums1:
        result.append(i)
    for j in nums2:
        result.append(j)
    result = sorted(result)
    temp = result.__len__()//2
    median = result[temp]
    if result.__len__() % 2 == 0:
        median = (result[temp]+result[temp-1])/2

    return median
nums1 = []
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))