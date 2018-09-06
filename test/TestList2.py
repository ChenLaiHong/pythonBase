# 列表常用操作
# 添加：append,添加到列表最后
nums1 = [1, 2, 3]

# print(nums1.append(5))
# print(nums1)

# insert(index.object) 任意位置插入,index:索引，到时会插入到这个索引之前，object想要添加的元素

# print(nums1.insert(2, "x"))
# print(nums1)
# print(nums1.insert(0, 9))
# print(nums1)

# extend (iterable):往列表中扩展另外一个可迭代序列
# iterable:可迭代集合、字符串、列表、元组....

num2 = ['a', 'b', 'c']
# print(nums1.extend(num2))
# print(nums1)

# 乘法运算:只能乘一个数，相当于循环，重复几遍

# print(nums1 * 3)

# 加法运算，相当于extend,但是其原列表不改变
# 区别;extend可以算是两个集合的拼接，append是把一个元素追加到一个集合后
print(nums1 + num2)
print(num2)
print(nums1)

# 删除操作
# del 指定元素
del nums1[1]
print(nums1)

# 删除整个列表
num3 = [8, 9, 10]
# del num3

# pop(index-1):移除并返回列表中指定索引对应元素;index:需要被删除返回元素的索引
print(num3.pop(1))
print(num3)

# remove(object)移除指定元素,从左往右删除，只删除一个
print(num3.remove(8), num3)

# 注意：不能在循环中执行remove操作，删除不干净
num4 = [1, 2, 2, 3, 4, 2, 2]
# for number in num4:
#     if number == 2:
#         num4.remove(2)
# print(num4)

# 修改
num4[2] = 66
print(num4)

# 查询
# 获取单个元素items[index],注意负索引
print(num4[3])
print(num4[-1])

# 获取元素索引
print(num4.index(4))

# 获取指定元素个数
print(num4.count(2))

# 获取多个元素，切片.items[start:end:step]。[start,end)
num5 = [1, 3, 2, 4, 5, 8, 6, 7]
print(num5[0:5:2])
# 反转整个列表
print(num5[::-1])

# 遍历
# 根据元素进遍历
#   for item in list:
# print(item)
for item in num4:
    print(item, end=" ")

# 根据索引进行遍历
# for index in range(len(list)):
#     print(index-1,list[index-1])
for index in range(len(num4)):
    print(index - 1, num4[index - 1])

# 枚举类型
values = ["a", "b", "c", "d", "e", "f"]
# 创建一个枚举对象
print(list(enumerate(values)))
# 遍历整个枚举对象
# tuplevalue元组
# for idx, val in enumerate(values):
for tuplevalue in enumerate(values):
    # print(tuplevalue)
    idx, val = tuplevalue
    print(idx, val)

# 判定是否为可迭代对象
import collections

print(isinstance(num4, collections.Iterable))

# 列表的判定
# 元素 in 列表
# 元素 not in 列表
print(1 in num4)
print(5 not in num4)

# 排序,没有改变本身
# sorted(iterable,key=None,reverse=False)
# iterable可迭代对象，key排序关键字，reverse控制升序降序，默认升序
print(sorted(num4))
print(sorted(num4, reverse=True))
print(num4)

# 根据元组里的第一个值进行排序
s = [("zs", 18), ("zs1", 16), ("zs3", 14), ("zs2", 17), ("zs5", 19)]
print(sorted(s))


# 按照指定元素排序
def getKey(x):
    return x[1]


print(sorted(s, key=getKey))

# 改变本身，只能操作列表
l = [1, 3, 6, 2, 4, 9, 7]
res = l.sort()
print(res, l)
result = s.sort(key=getKey)
print(result, s)

import random
# 乱序，导入random模块。random.shuffle(list),改变本身
num6 = [1, 2, 3, 4, 5, 6]
random.shuffle(num6)
print(num6)

# 反转 reverse()
print(num6.reverse(),num6)



