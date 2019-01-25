"""
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
示例 1:
输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]
示例 2:
输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]
说明:
    k 的值为正数，且总是小于给定排序数组的长度。
    数组不为空，且长度不超过 104
    数组里的每个元素与 x 的绝对值不超过 104
"""
import math
def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    flag = 1
    dict_temp = {}
    for i in arr:
        dict_temp[str(flag)+"&"+str(i)] = abs(x-i)
        flag += 1
    result = sorted(dict_temp.items(),key=lambda n: int(n[0].split("&")[0]))

    result = sorted(result, key=lambda n: n[1])
    temp_list = [result[i][0] for i in range(k)]
    final = []
    for i in temp_list:
        temp = i.split("&")
        final.append(int(temp[1]))
    return sorted(final)
    # return result
print(findClosestElements([1,2,5,5,6,6,7,7,8,9], 7, 7))
