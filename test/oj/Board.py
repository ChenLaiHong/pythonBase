"""
Description
给定一块蛋糕的宽度X,Y，你需要判断是否能否切成特定的形状
Input
第一行包括测试用例的数量N，接下来对于每一个测试用例：
第一行包括X, Y, M (M≤100000)，对于接下来的M行，每一行有X 和 Y代表需要切成的形状；
Output
如果可以输出：Sim
不行输出：Nao
Sample Input 1
2
10 10 3
5 5
10 10
5 25
2 3 1
3 2
Sample Output 1
Sim
Sim
Nao
Sim
Sample Input 2
1
10 10 5
11 10
10 11
9 10
10 9
10 10
Sample Output 2
Nao
Nao
Sim
Sim
Sim
"""
def check(input_list, X, Y):
    if int(input_list[0]) <= X and int(input_list[1]) <= Y or int(input_list[0]) == Y and int(input_list[1]) == X:
        return True
    else:
        return False
num = int(input())
while num > 0:
    X, Y, M = input().split()
    X, Y, M = int(X), int(Y), int(M)
    for i in range(M):
        temp = input().split()
        if check(temp,X,Y):
            print("Sim")
        else:
            print("Nao")
    num -= 1