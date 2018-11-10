"""
Grace Murray Hopper，也被称为“COBOL的奶奶”，在20世纪40年代和50年代担任系统分析师和美国海军上将。Grace创建了Flow-Matic编程语言，
作为创建COBOL的基础，此外，她还参与了第一个COBOL编译器的创建。术语BUG一直用于代表计算机程序的错误。Grace Hopper是计算机史上最重要
的女性之一，Grace Hopper被用于庆祝女性计算机的胜利。

这个问题中，在每个由连字符分隔的测试行中给出五个单词。
对于每一行，如果在每个单词的开头或结尾按顺序找到形成单词COBOL的字母，则将打印“GRACE HOPPER”字样。如果找不到，则会打印“BUG”字样。
该条目包含几个测试用例。每个测试用例由一行包含1到50个字符组成，由小写字母和大写字母组成（'a' - 'z'，'A' - 'Z'）和连字符（' - '），没有空格。
Output
对于每个测试用例，请打印相应的单词。
Sample Input 1
6
cap-one-best-opinion-language
Ana-number-once-a-night
fantastic-officio-dumb-onto-label
historic-opposite-ball-photo-real
Caio-init-bug-bing-love
corner-octal-bond-ago-pencil
Sample Output 1
GRACE HOPPER
BUG
GRACE HOPPER
GRACE HOPPER
BUG
GRACE HOPPER
"""
def find(nums):
    temp = "COBOL"
    n = 0
    flag = 0
    for i in nums:
        if i[0].upper() == temp[flag] or i[len(i)-1].upper() == temp[flag]:
            n += 1
        flag += 1
    if n == 5:
        return "GRACE HOPPER"
    else:
        return "BUG"
N = int(input())
result = []
while N > 0:
    nums = input().split("-")
    result.append(find(nums))
    N -= 1
for i in result:
    print(i)