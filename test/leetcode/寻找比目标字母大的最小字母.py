"""
给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
示例:
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"
输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"
输入:
letters = ["c", "f", "j"]
target = "d"
输出: "f"
输入:
letters = ["c", "f", "j"]
target = "g"
输出: "j"
输入:
letters = ["c", "f", "j"]
target = "j"
输出: "c"
输入:
letters = ["c", "f", "j"]
target = "k"
输出: "c"
"""
def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    temp = letters.copy()
    temp.append(target)
    temp = sorted(set(temp))
    if temp[len(temp)-1] == target:
        return temp[0]
    else:
        return temp[temp.index(target)+1]
print(nextGreatestLetter(["c","f","j"],"a"))

