"""
问题描述
　　小明带着N元钱去买酱油。酱油10块钱一瓶，商家进行促销，每买3瓶送1瓶，或者每买5瓶送2瓶。请问小明最多可以得到多少瓶酱油。
输入格式
　　输入的第一行包含一个整数N，表示小明可用于买酱油的钱数。N是10的整数倍，N不超过300。
输出格式
　　输出一个整数，表示小明最多可以得到多少瓶酱油。
样例输入
40
样例输出
5
样例说明
　　把40元分成30元和10元，分别买3瓶和1瓶，其中3瓶送1瓶，共得到5瓶。
样例输入
80
样例输出
11
样例说明
　　把80元分成30元和50元，分别买3瓶和5瓶，其中3瓶送1瓶，5瓶送2瓶，共得到11瓶。
"""

money = int(input())
result = 0
moneyList = [50, 30, 10]
numList = [7, 4, 1]
n = 0
while n < 3 and money >= 10:
    if money >= moneyList[n]:
        result += (money // moneyList[n])*numList[n]
        money -= (money // moneyList[n])*moneyList[n]
    n += 1

# ------------第一的有点臃肿了代码，上面是优化了的----------
# while money >= 10:
#     if money >= 50:
#         result += (money // 50)*7
#         money -= 50*(money // 50)
#         continue
#     elif money >= 30:
#         result += (money // 30)*4
#         money -= 30*(money // 30)
#         continue
#     elif money >= 10:
#         result += (money // 10)
#         money -= 10*(money // 10)
print(result)