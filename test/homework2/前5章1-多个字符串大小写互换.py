"""
【问题描述 】
    将输入的字符串中，大写字母转换为小写字母，小写字母转换为大写字母。
【输入格式 】
第一行包含一个整数n，表示给出的文字的行数。
接下来n行，每行包含一个字符串，字符串由大小写英文字母组成，不含空格和其他字符。  
【输出格式 】
    输出字符串，为输入字符串的大小写转换
【样例输入 】
3
HelloWorld
HiHiHelloHiHi
GrepIsAGreatTool
【样例输出】
hELLOwORLD
hIhIhEELOhIhI
gREPiSagREAtOOL
【样例输入 】
3
UxTsda
ApIogRvFGge
DogcAtaNdchIck
【样例输出】
uXtSDA
aPiOGrVfgGE
dOGCaTAnDCHiCK
【样例输入 】
4
pwHjISls
WiPNMswh
poSjhzna
ewieShas
样例输入
PWhJisLS
wIpnmSWH
POsJHZNA
EWIEsHAS
"""
num = int(input())
for i in range(num):
    print(input().swapcase())
