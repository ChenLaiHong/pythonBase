"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
"""
def find(s, result):
    length = s.__len__() % 2
    temp = s.__len__() // 2
    if length == 0:
        last = s[temp:s.__len__()]
        if s[0:temp] == last[::-1]:
            result.add(s)
    else:
        last = s[temp+1:s.__len__()]
        if s[0:temp] == last[::-1]:
            result.add(s)
    return result

# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     if s != "" and len(s) > 1:
#         result = set()
#         for i in range(s.__len__()-1):
#             for j in range(i+1, s.__len__()+1):
#                 s1 = s[i:j]
#                 length = s1.__len__() % 2
#                 temp = s1.__len__() // 2
#                 if length == 0:
#                     last = s1[temp:s1.__len__()]
#                     if s1[0:temp] == last[::-1]:
#                         result.add(s1)
#                 else:
#                     last = s1[temp+1:s1.__len__()]
#                     if s1[0:temp] == last[::-1]:
#                         result.add(s1)
#
#         temp1 = list(result)
#         length = []
#         for i in temp1:
#             length.append(len(i))
#         res = temp1[length.index(max(length))]
#         return res
#     else:
#         return s

def longestPalindrome(s):
    n = len(s)
    maxL, maxR, max = 0, 0, 0
    for i in range(n):
        # 长度为偶数的回文字符串
        start = i
        end = i + 1
        while start >= 0 and end < n:
            if s[start] == s[end]:
                if end - start + 1 > max:
                    max = end - start + 1
                    maxL = start
                    maxR = end
                start -= 1
                end += 1
            else:
                break

        # 长度为奇数的回文子串
        start = i - 1
        end = i + 1
        while start >= 0 and end < n:
            if s[start] == s[end]:
                if end - start + 1 > max:
                    max = end - start + 1
                    maxL = start
                    maxR = end
                start -= 1
                end += 1
            else:
                break
    return s[maxL:maxR+1]

print(longestPalindrome("cbbd"))