"""
【问题描述】去掉字符串s中的指定字符，并将新得到的字符串输出。
【输入形式】一个字符串，和要去掉的字符（两者中间有一个空格）
【输出形式】去掉特定字符后的新字符串
【样例输入】abdsag d
【样例输出】absag
【样例说明】要去除指定字符的全部出现。
"""
s = input().split()
temp = s[0]
tempResult = []
count = temp.count(s[1])
for i in temp:
    tempResult.append(i)
while count > 0:
    for i in tempResult:
        if i == s[1]:
            tempResult.remove(i)
            count -= 1
            break
result = ""
for i in tempResult:
    result += i
print(result)
