"""
【问题描述】输入两个正整数a和b（0<a，b<1000000），求出其最大公约数和最小公倍数并输出。
【输入文件】从标准输入读取一行，是两个整数a和b，以空格分隔。
【输出文件】向标准输出打印以空格分隔的两个整数，分别是a、b的最大公约数和最小公倍数。
【输入样例】12 18
【输出样例】6 36
【样例说明】12和18的最大公约数是6，最小公倍数是36.
"""

def yue(num1, num2):
    xiao = num1 if (num1 < num2) else num2
    while True:
        if num1 % xiao == 0 and num2 % xiao == 0:
            result = xiao
            break
        xiao -= 1
    return result
def bei(num1, num2):
    da = num1 if (num1 > num2) else num2
    while True:
        if da % num1 == 0 and da % num2 == 0:
            result = da
            break
        da += 1
    return result

a, b = input().split()
print(yue(int(a), int(b)), bei(int(a), int(b)))