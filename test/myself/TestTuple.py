# 列表是有序的可变的元素集合，元组是有序的不可变的元素集合
# 一个元素的写法,一定要写上后面的逗号
num = (1,)
print(type(num))

# 多个元素的写法，用逗号隔开，最后不需要逗号结尾
num1 = ("abc", [1, 2], 3)
print(type(num1))

# 多个对象以逗号分隔，默认为元组
num2 = 1, 2, 3, "zs"
print(type(num2))

# 从列表转换成元组,tuple(seq)，不改变本身
num3 = [1, 2, 3]
print(tuple(num3), type(num3))

# 元组的嵌套
num4 = (1, 2, ("a", "b"))
print(type(num4))

# 查找
# 获取单个元素
print(num4[0])
# 获取多个元素，切片tuple[start:end:step]
print(num1[0: 3])

# 反转
print(num1[::-1])

# 获取,
#   tuple.count(item):统计指定元素的个数，元素不存在则返回0
#   tuple.index(item):获取指定元素的索引
#   len(tup)：返回元组中元素的个数
#   max(tup)：返回元组中最大的值
#   min(tup)：返回元组中最小的值
num5 = (1, 5, 3, 4, 8, 9, 5, 3, 4, 6, 7)
print(num5.count(5), num5.index(3), len(num5), max(num5), min(num5))

# 判定元素
# 元素 in 元组
# 元素 not in 元组
print(5 in num5, 0 not in num5)

# 拼接
# 乘法：（元素1，元素2...）* int 类型数值
#       =（元素1，元素2...，元素1，元素2...，...）
# 加法：（元素1，元素2）+（元素3，元素4）
#       =（元素1，元素2，元素3，元素4）
print(num1*3)
print(num5+num)

# 拆包
#  a, b = (1, 2)
#     a = 1
#     b = 2
a, b = (10, 20)
print(a, b)



