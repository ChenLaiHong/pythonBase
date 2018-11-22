"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
输入列子1：2
输出例子1：2
输入列子2：10
输出例子2：512
输入例子3：5
输出例子3：16
"""
def jump(step):
    result = 0
    if step == 0:
        result = 0
    elif step == 1:
        result = 1
    else:
        result = 2 * jump(step-1)
    return result

num = int(input())
print(jump(num))
