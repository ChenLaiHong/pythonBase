"""
【问题描述】
先输入多个英文单词及其译文，接着输入英文单词，输出该单词的译文。
【输入形式】
第一行是整数n，表示n个英文单词及其译文。
接下来输入n行是英文单词和译文，中间用空格隔开。
接下来输入的一行是一个英文单词。
【输出形式】
输出最后输入的英文单词的译文。如果没有检索到该单词，输出"not found"。
【样例输入】
3
word zi
go qu
input shuru
go
【样例输出】
qu
【样例说明】
qu是go单词的译文。
"""
words = []
yiwen = []
wordsDict = {"word": words, "yiwen": yiwen}
num = int(input())
while num > 0:
    temp = input().split()
    words.append(temp[0])
    yiwen.append(temp[1])
    num -= 1
find = input()
if find in wordsDict["word"]:
    wordIndex = wordsDict["word"].index(find)
    print(wordsDict["yiwen"][wordIndex])
else:
    print("not found")