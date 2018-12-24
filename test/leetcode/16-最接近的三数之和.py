"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
def threeSumClosest(nums, target):
    nums.sort()
    res = None
    for i in range(len(nums)):
        if i == 0 or nums[i] > nums[i-1]:
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                res = s if res == None or abs(s-target) < abs(res-target) else res
                if s == target:
                    return s
                elif s > target:
                    r -= 1
                else:
                    l += 1
    return res
print(threeSumClosest([-1,2,1,-4],1))
