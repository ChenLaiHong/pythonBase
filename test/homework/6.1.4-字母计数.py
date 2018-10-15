"""
【问题描述】
输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。
【输入形式】
一个字符串。
【输出形式】
出现次数最多的字母及其出现次数
【样例输入】
abcccd
【样例输出】
c 3
"""
words = {}
strInput = input()
for i in range(strInput.__len__()):
    words[strInput[i]] = strInput.count(strInput[i])

a1 = sorted(words.items(), key=lambda x: x[1], reverse=True)

num = [n[-1] for n in a1]
maxNum = max(num)
result = []
for i in a1:
    if i[-1] == maxNum:
        result.append(i[0]+" "+str(maxNum))

for i in sorted(result):
    print(i)