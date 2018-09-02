number1 = 4
number2 = 9
number1, number2 = number2, number1
# 连接不像java，这里还要把类型转换成str类型才可以连接
print("number1:" + str(number1))
print(number2)

# python3中的input语句是直接输入str类型，下面语句是将str转成了int
# 要输出int类型也可以使用eval函数,例如：eval(input("请输入一个分数："))
score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 60 > score >= 0:
    print('C')
else:
    print("输入错误！")

# 三元操作符,取两数中的最大值
x, y = 4, 5
small = y if x < y else x
print(small)

# while循环
i = 5;
while i < 10:
    i = i + 1
    print(i)

# for循环
name = 'name'
for i in name:
    print(i, end=' ')

print()
# 列表
member = ['小明', '小鱼儿', '张三丰', '玉树临风']
for each in member:
    print(each, len(each))

print()

# 循环输出从2到9，包含2不包含9
for i in range(2, 9):
    print(i)


