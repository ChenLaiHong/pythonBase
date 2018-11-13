"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,3,2]
输出: 3
示例 2:
输入: [0,1,0,1,0,1,99]
输出: 99
"""
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    temp = list(set(nums.copy()))
    for i in range(len(temp)//2):
        if nums.count(temp[i]) == 1 or nums.count(temp[len(temp)-i-1]) == 1:
            if nums.count(temp[i]) == 1:
                return temp[i]
            else:
                return temp[len(temp)-i-1]
nums = input().split(",")
print(singleNumber(nums))