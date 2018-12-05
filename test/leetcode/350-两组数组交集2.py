"""
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：
    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
    我们可以不考虑输出结果的顺序。
"""
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1) < len(nums2):
        duan = nums1
        chang = nums2
    else:
        duan = nums2
        chang = nums1
        if len(nums1) == len(nums2):
            duan = list(set(nums1)) if len(set(nums1)) < len(set(nums2)) else list(set(nums2))
            chang = list(set(nums2)) if len(set(nums1)) < len(set(nums2)) else list(set(nums1))
    result = []
    for i in set(duan):
        if i in chang:
            flag = duan.count(i) if duan.count(i) < chang.count(i) else chang.count(i)
            for j in range(flag):
                result.append(i)
    return result
print(intersect([1], [1]))
