"""
【问题描述】编写程序判断字符c是否在字符串str中出现。
【输入形式】需查找的字符c 和 搜索字符串str
【输出形式】true或者false
【样例输入】m akdfomdkl
【样例输出】true
【样例说明】输出true或者false，不是1或者0
"""
c, str = input().split()
if c in str:
    print("true")
else:
    print("false")
