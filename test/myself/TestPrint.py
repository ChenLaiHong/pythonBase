# 输出语句
# 直接输出一个值
print(123)

# 输出一个变量
num = 66
print(num)

# 输出多个变量用逗号隔开
num2 = 44
print(num, num2)

# 格式化输出
name = "张三"
age = 20
print("我的名字是%s,年龄是%d" % (name, age))
print("我的名字是{0},年龄是{1}". format(name, age))

# 输出到文件中
f = open("test.txt", "w",encoding='utf-8')
print("你好啊", file=f)

# 输出不自动换行
print("不换行", end="")

# 使用各个数据用分隔符进行分割
print(1, 2, 3, sep="&")