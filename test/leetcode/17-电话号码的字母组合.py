"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    def haha(str1, str2):
        res = []
        for i in range(len(str1)):
            for j in range(len(str2)):
                res.append(str1[i] + str2[j])
        return res
    dict = {"1": "1", "2": "abc", "3": 'def', "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    l = len(digits)
    ult = []
    for i in range(l):
        if i == 0:
            y = dict.get(digits[i])
            for x in range(len(y)):
                ult.append(y[x])
        else:
            ult = haha(ult, dict.get(digits[i]))
    return ult

print(letterCombinations("23"))