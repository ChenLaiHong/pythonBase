"""
【问题描述】
生词本包含多个条目。每个条目由生词和该生词的含义组成。例如，生词name的含义是名字。编写程序，输出多个生词及其含义，
列出生词本中包含的生词及其含义。
【输入形式】
输入多行。每一行包含生词及其含义。这一行内，生词和含义之间用冒号分隔。
【输出形式】
输出多行。每一行列出所有的生词及其含义，之间用空格分隔。生词按字典序从小到大排序。
【样例输入】
name:mingzi
hello:nihao
python:manshe
【样例输出】
hello nihao
name mingzi
python manshe
"""
import sys

result = {}
while True:
    nums = sys.stdin.readline().strip()
    if nums == "":
        break
    temp = nums.split(":")
    result[temp[0]] = temp[1]
temp = sorted(result)
for i in temp:
    print(i, result[i])