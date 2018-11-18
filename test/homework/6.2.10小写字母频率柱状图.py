"""
【问题描述】
编写程序从标准输入中读入一段英文，统计其中小写字母出现次数，并以柱状图的形式显示其出现次数。
【输入形式】
在标准输入上输入一段英文文章（可能有一行，也可能有多行），在新的一行的开头输入ctrl+z键或者Ctr+D键表示结束。
【输出形式】
在屏幕上依次输出表示每个小写字母出现次数的柱状图（以*字符表示柱状图，空白处用空格字符表示，某个小写字母出现多少次，
就显示多少*字符；柱状图的高度以出现最多的字母次数为准），在最后一行依次输出26个小写字母。
【样例输入】
The computing world has undergone a
revolution since the publication of
The C Programming Language in 1978.

"""
import sys
lines = ''
while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    lines += line

lower_cnt_dict = {}
for i in range(26):
    ch = chr(ord('a') + i)
    lower_cnt_dict[ch] = 0

for ch in lines:
    if ch.isalpha() and ch.islower():
        lower_cnt_dict[ch] += 1

max_cnt = 0
for cnt in lower_cnt_dict.values():
    if max_cnt < cnt:
        max_cnt = cnt

diagram = []
for i in range(max_cnt):
    diagram.append([' '] * 26)

for c in range(26):
    ch = chr(ord('a') + c)
    cnt = lower_cnt_dict[ch]
    for r in range(cnt):
        diagram[max_cnt - r - 1][c] = '*'

for r in range(max_cnt):
    print(''.join(diagram[r]))
for c in range(26):
    ch = chr(ord('a') + c)
    print(ch, end='')