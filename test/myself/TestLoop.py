# while循环,跟java差不多
# 输出10次“人生苦短，我学Python”

num = 0
while num < 10:
    print("人生苦短，我学Python")
    num += 1

# 计算1到10的和,这里使用break，执行完一次循环就跳出了循环，但是打印语句还是会执行
sumNumber = 0
number = 1
while number <= 10:
    sumNumber += number
    number += 1
    # break
print(sumNumber)

# while与else与break连用
# 当不使用break是，循环执行完便会执行else的语句
# 使用了break的话，执行一次就结束了整个循环，else里面的也没有输出
num = 0
while num < 10:
    num += 1
    print("人生苦短，我学Python")
    # break
else:
    print("整个循环结束")


# for循环
# 格式：
# for x in xxx:
# xxx通常是一个集合，x就是取出集合里面的每一个元素赋值给变量x

# 例子：将“人生苦短，我学Python”里的每个字符打印出来
notic = "人生苦短，我学Python"
for x in notic:
    print(x, end="、")

# 列表
# len函数就是输出某个的长度
member2 = ['小明', '小鱼儿', '张三丰', '玉树临风']
for name in member2:
    print(name, len(name))

# for循环中与break，else连用跟while的是一样的


# 反转字符串
result = ""
for c in notic:
    result = c + result
print(result)

# 打印1到100的偶数
number2 = 1
while number2 <= 100:
    if number2 % 2 == 0:
        print(number2, end="、")
    number2 += 1

print()
for n in range(1, 101):
    if n % 2 == 0:
        print(n, end="、")

print()
# python中的break与continue跟java中使用是一样的
for a in range(1, 11):
        if a == 6:
            break
        print(a, end=" ")

print()

for b in range(1, 11):
    if b == 6:
        continue
    print(b, end=" ")




