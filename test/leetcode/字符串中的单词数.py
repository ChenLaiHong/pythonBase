"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。
示例:
输入: "Hello, my name is John"
输出: 5

"""
wordList = input().split()
print(wordList.__len__())
# temp = ""
# result = []
# flag = True
# for w in range(wordList.__len__()):
#
#     if wordList[w] != "," and wordList[w] != " " and w != wordList.__len__():
#         temp += wordList[w]
#     else:
#         if temp != "":
#             result.append(temp)
#             temp = ""
#
# print(result.__len__())