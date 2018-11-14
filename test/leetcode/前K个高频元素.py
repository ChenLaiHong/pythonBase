"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
说明：
    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    tempDict = {}
    for i in range(len(nums)):
        if nums[i] in tempDict:
            tempDict[nums[i]] = tempDict[nums[i]] + 1
        else:
            tempDict[nums[i]] = 1
    result = list(sorted(tempDict.items(), key=lambda n: n[1], reverse=True))
    num = [n[0] for n in result]
    return num[0:k]
nums = [1]


k = 1
print(topKFrequent(nums, k))