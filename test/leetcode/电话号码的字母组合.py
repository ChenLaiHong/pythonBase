"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
number = [2, 3, 4, 5, 6, 7, 8, 9]
word = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
num = input().strip()

def link(numList1, numList2):
    result = []
    for i in numList1:
        for j in numList2:
            result.append(i+j)
    return result

temp = []
if num.__len__() == 1:
    for i in word[number.index(int(num[0]))]:
        temp.append(i)
if num.__len__() > 1:
    temp = word[number.index(int(num[0]))]
    for i in range(1, num.__len__()):
        temp = link(temp, word[number.index(int(num[i]))])
print(temp)

