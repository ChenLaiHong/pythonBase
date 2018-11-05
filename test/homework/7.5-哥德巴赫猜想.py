"""
【问题描述】
证明在偶数n以内，歌德巴赫猜想是成立的。歌德巴赫猜想是：任何一个充分大的偶数都可以表示为两个素数之和。
例如,4=2+2   6=3+3   8=3+5  50=3+47。
【输入形式】
输入偶数n
【输出形式】
对每一个偶数4, 6, 8, ..., n，依次输出一行。该行内容是<偶数>=<素数1>+<素数2>，要求素数1<=素数2.
【样例输入】
6
【样例输出】
4=2+2
6=3+3
"""
def sushu(num):
    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False

number = int(input())
num = 4

while num <= number:
    flag = 0
    for i in range(2, number):
        for j in range(i, number):
            if sushu(i) and sushu(j) and i+j == num:
                print("%d=%d+%d" % (num, i, j))
                flag = 1
        if flag == 1:
            break
    num += 2







