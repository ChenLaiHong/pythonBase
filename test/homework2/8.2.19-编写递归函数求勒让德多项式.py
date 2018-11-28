"""
【问题描述】
编写递归函数P(n,x)实现勒让德多项式:
(n+1)*P（n+1, x) = (2n+1)*x*P(n, x)-n*P(n-1, x)
函数名字为P，参数为n和x，其中P(0,x)=1，P(1,x)=x。
在输入框內填写函数定义，形成完整的程序。
"""
def P(n, x):
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        return (2*n+1)*x*P(n, x)-n*P(n-1, x)

n_str, x_str = input().split()
n = int(n_str)
x = float(x_str)
print("%.3f" % P(n, x))