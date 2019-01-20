"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:return 0
    dp = [1]*len(nums)
    res = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j] + 1)
        res = max(res,dp[i])
    return res
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))


