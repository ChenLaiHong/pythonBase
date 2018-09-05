# 字符串切片操作
# 字符串下标可以为负数但是不能超过长度减1
name = "abcdefgbhk age name"
print(name[0])
# 下标为负数就是从字符串后面开始数
print(name[-1])

# 获取字符串片段：name[起始:结束:步长]，获取范围[起始，结束)，默认步长为1
# 步长> 0，从左到右；步长< 0,从右到左。注意：不能从头部跳转到尾部，也不能从尾部跳转到头部
print(name[0:3])
print(name[4:1:-1])

# 反转字符串
print(name[::-1])

# len(x):计算字符串的字符个数,转义字符占一个
print(len(name))

# find(sub,start=0,end=len(str))：查找字符索引位置[start,end)
print(name.find("bc"))
print(name.find("b", 3))
print(name.find("b", 4, 7))

# rfind ：功能跟find一样，只不过这个是从右往左查找
print(name.rfind("b"))

# index 获取某字符，跟find差不多，find在找不到就返回-1，而index则报错
# print(name.index("xx"))

# rindex 跟index一样，只是从右往左
# print(name.rindex("xx"))

# count(sub,start,end=len(str)),计算某个字符串出现的个数
print(name.count("b"))

# 转换操作
# replace(old,name[,count]):给定新字符串替换原字符串中的旧字符
# old :需要被替换的旧字符；new :替换后的新字符；count ：替换的个数，省略则表示替换全部
# 返回替换后的字符串，但是并不会改变原字符串本身
print(name.replace("b", "w"))
print(name.replace("b", "w", 1))

# capitalize()返回首字母大写后的新字符串，并不会改变字符串本身
print(name.capitalize())

# title()返回每个单词首字母大写后的新字符串，不会改变本身
print(name.title())

#lower():将字符串每个字符变小写
name1 = "Wo Xue Python"
print(name1.lower())

#upper():将所有字母变成大写
print(name1.upper())


# 字符串填充压缩操作

