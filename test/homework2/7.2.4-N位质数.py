"""
【问题描述】给定一个整数N（2 <= N <= 8），生成所有的具有下列特性的特殊的N位质数，即其前任意位都是质数。
例如，7331即是这样一个4位的质数，因为7、73和733也都是质数。
【输入形式】输入一个整数N（2 <= N <= 8）。
【输出形式】输出有若干行，每行有一个整数，该整数有N位，而且其前任意位都是质数。并且：
1.要求输出所有符合题意的质数。
2.从小到大按顺序输出，且所有行上的数字不得重复。
【样例输入】2
【样例输出】
23
29
31
37
71
73
79

【样例说明】输出2位的质数，而且其前的任何一个数也是质数。"""
from itertools import count
def isPrime(n):
    n = int(n)
    if n <= 1:
        return "0"
    for i in count(2):
        if i * i > n:
            return "1"
        if n % i == 0:
            return "0"

N = int(input())
zuixiao = "1"
zuixiao += "0" * (N-1)
zuida = "9" * N
result = []

for i in range(int(zuixiao)+1, int(zuida)+1, 2):
    num = 1
    temp = []
    while num < N+1:
        if isPrime(str(i)[0:num]) == "0":
            break
        temp.append(isPrime(str(i)[0:num]))
        num += 1
    if temp.__len__() != N:
        continue
    result.append(i)
for i in result:
    print(i)