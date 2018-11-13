"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp = set(nums.copy())
    result = {}
    for i in temp:
        result[i] = nums.count(i)

    f = result.items()
    temp1 = sorted(f, key=lambda n: n[1], reverse=True)
    return temp1[0][0]

nums = input().split(",")

print(majorityElement(nums))