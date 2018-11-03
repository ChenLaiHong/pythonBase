"""
Description
有同学要换1分、2分、5分的硬币，他拿钱到银行去换，要求1分、2分、5分硬币至少各一枚，给银行一定的纸币后（以分为单位），银行可有多少种换法。
Input
输入纸币面值n
Output
输出换法种类
Sample Input 1
10
Sample Output 1
2
Sample Input 2
30
Sample Output 2
34
"""
n = int(input())
sum = 0
for i in range(1, n//5 + 1):
    for j in range(1, (n-i*5)//2 + 1):
        result = n - i*5 - j*2
        if result >= 1:
            sum += 1
print(sum)