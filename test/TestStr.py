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

# lower():将字符串每个字符变小写
name1 = "Wo Xue Python"
print(name1.lower())

# upper():将所有字母变成大写
print(name1.upper())


# 字符串填充压缩操作
# ljust(width,fillchar)表示原字符串靠左。width:指定结果字符串的长度；fillchar:
# 如果原字符串长度 < 指定长度时，填充过去的字符；返回填充完毕的字符
# 填充的字符是一个字符
name2 = " abwwoolcoo"
print(name2.ljust(18, "x"))

# rjust(width,fillchar)原字符串靠右，跟rjust差不多
print(name2.rjust(16, "x"))

# center(width,fillchar)原字符在中间，不能平分时右边比左边多
print(name2.center(18, "x"))

# lstrip(chars):从左侧开始移除指定的存在的字符(单个看),遇到不是指定的字符时就返回
print(name2.lstrip())

# rstrip(chars):从右侧开始移除指定字符
print(name2.rstrip("co"))

# 字符串的分割拼接
# split(sep,maxsplit):将一个大的字符串分割成几个子字符串
# sep:分隔符；maxsplit:最大分割次数，默认为有多少分多少，返回子字符串组成的列表
info = "zs-18-178-0220-6658456"
print(info.split("-"))
print(info.split("-", 3))

# partition(sep),根据指定的分隔符将字符串分成三部分（分隔符左侧内容，分隔符，分隔符右侧内容）
# 返回一个元组类型
print(info.partition("-"))

# rpartition(sep)从右边找，跟partition很像
print(info.rpartition("-"))

# splitlines(keepends)按照换行符（\r,\n）将字符串拆成多个元素，保存在列表中
# keepends:是否保留换行符，bool类型
info2 = "wo \n xue \r python"
print(info2.splitlines())

# join(iterable):iterable可迭代的对象：字符串、元组、列表。将给定的可迭代对象进行拼接
items = ["wo", "xue", "python"]
print("-".join(items))

# 字符串判定操作
# isalpha(),判断字符串中所有字符是否都是字母

print("abc".isalpha())
print(name.isalpha())
# isdigit(),判断字符串中所有字符都是数字
print("15632".isdigit())
print(name.isdigit())

# isalnum()是否是数字或字母
print("123abc".isalnum())

# isspace()字符串中是否所有字符都是空白符包括空格、缩进、换行等不可见转义符
print(" ".isspace())
print(name2.isspace())

# startwith(prefix,start=0,end=len(str))：判定一个字符串是否以某个前缀开头
# prefix:需要判定的前缀字符串；start：判定起始位置（能取到）；end：判定结束位置（不包括）
print(name.startswith("a"))
print(name.startswith("a", 3, 7))

# endwith(prefix,start=0,end=len(str)):判定一个字符串以某个后缀结束
print(name.endswith("e"))

# in 判定一个字符串，是否被另一个字符串包含
# not in 判定一个字符串，是否不被另一个字符串包含





