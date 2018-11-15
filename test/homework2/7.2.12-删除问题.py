"""
【问题描述】输入一个高精度的大正整数S（S最长可达240位），去掉其中任意N位数字后剩下的数字按原次序组成一个新的正整数S'。
编程对给定的N和S，寻找一种方案使得剩下的数字组成的新数S'最小。
【输入形式】输入有两行：
1.第一行是大整数S。其中S最长可达240位。
2.第二行是整数N。S、N均以非0数字开头。
【输出形式】输出有一行，是在S中删除N位后所得的最小数字S'。
【样例输入1】
178543
4
【样例输出1】13
【样例输入2】
1002
1
【样例输出2】002
【样例说明】样例1中输入整数S=178543，N=4，要求在178543中删除4位，使剩下的数字最小。正确答案为S' = 13。
样例2中输入整数S＝1002，N＝1，删完一位后S'= 002，而不是2，即2之前的0也必须输出。
【运行时限】程序一次运行的最长时间限制在15秒内，超出则认为程序错误。
【算法提示】将整数看作字符串形式读入；删数时，从前往后寻找第一个比后一个数字大的数字，然后删除之，按照这种方法删除N个数字即得最小数字。
"""

def change(temp):
    string = ""
    for i in temp:
        string += str(i)
    return string
def find(temp):
    numsindex = temp.index(min(temp))
    return numsindex
S = input()
N = int(input())
zuixiao = int(S)
flag = -1
temp = [int(i) for i in S]
if N == 1:
    for i in range(len(temp)):
        tempCopy = temp.copy()
        for j in range(i, len(temp)):
            tempCopy.remove(temp[j])
            final = int(change(tempCopy))
            if final < zuixiao:
                flag = j
                zuixiao = final
            break
    for i in range(len(temp)):
        if i != flag:
            print(temp[i], end="")
else:
    n = 1
    z = temp.index(min(temp))
    string = str(temp[z])
    tempList = temp[z+1:len(temp)]
    while n < len(S) - N:
        if len(tempList) > 0:
            strnum = find(tempList)
            string += str(tempList[strnum])
            tempList = tempList[strnum+1: len(tempList)]
        n += 1
    print(string)





