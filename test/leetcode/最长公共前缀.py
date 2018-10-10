"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
"""
def longestCommonPrefix(strs):
    # w = input().split(",")
    # 记录列表中每个字符串的长度
    length = []
    for i in strs:
        length.append(len(i))
    # 字符串中最短的长度
    result = ""
    if length.__len__() > 0:
        small = min(length)
        flag = True
        for i in range(small):
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:
                    flag = False
                    break
            if flag:
                result += temp
            else:
                break
    return result

strs = ["dog", "dogracecar", "dogcar"]
print(longestCommonPrefix(strs))


