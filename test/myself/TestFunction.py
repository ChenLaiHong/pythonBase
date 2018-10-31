# 内建函数就相当于java中的默认导入的函数不需要显式使用关键字进行导入
# abs()返回绝对值
number = -52
print(abs(number))

# max()取得最大数
print(max(1, 8, 9, 3, 23, 41, 25))
print(max([1, 8, 9, 3, 23, 41, 25]))

# min()取得最小数
print(min(1, 8, 9, 3, 23, 41, 25))
print(min([1, 8, 9, 3, 23, 41, 25]))

# round()四舍五入
# 不保留小数
print(round(3.14))
# 保留一位小数
print(round(3.154, 1))

# pow(x,y)返回x的y次幂，相当于 x**y
print(pow(2, 3))
# pow(x,y,z)相当于：x**y % z
print(pow(2, 3, 5))

# math模块函数,使用格式：math.函数名称（参数）
import math

print(math.pow(4, 3))
# ceil()向上取整
print(math.ceil(3.15))
# floor()向下取整
print(math.floor(3.15))
# sqrt()开平方
print(math.sqrt(9))
# log(x,y)求对数,以y为底的对数,也就是y的多少次方等于x
print(math.log(8, 2))

# 随机数
import random
print("=================")
# random()[0,1)范围内的随机小数
print(random.random())

# choice(x)：从一个序列中随机挑选一个数值
seq = [1, 8, 6, 9, 3, 4]
print(random.choice(seq))

# uniform(x,y),[x,y]范围内的随机小数
print(random.uniform(1, 3))

# randint(x,y),[x,y]范围内的随机整数
print(random.randint(1, 15))

# randrange(start,stop=None,step=1),给定区间内一个随机整数[start,stop)
print(random.randrange(1, 15, 2))


# 三角函数
# 正弦函数：sin(x),x是一个弧度，例如30度的弧度= 30/180 * pi
hudu = 1/6 * math.pi
print(math.sin(hudu))
# degrees()把弧度变角度
print(math.degrees(60))
# radians()把角度变弧度
print(math.sin(math.radians(30)))



