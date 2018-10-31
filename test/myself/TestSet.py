# 集合：无序的，不可随机访问的，不可重复的元素集合
# 集合有可变集合和非可变集合
# set:可变集合，有增删改；forzenset：不可变集合，不可增删改

# 可变集合
s = {1, 2, 3}
print(s, type(s))

# s = set(iterable)可迭代对象是字典时，集合是其中的key值
s2 = set("abc")
print(s2, type(s2))

s3 = set({"name": "张三", "age": 18})
print(s3, type(s3))
# 推导式
s4 = set(x ** 2 for x in range(1, 10) if x % 2 == 0)
print(s4, type(s4))

# 不可变集合
# fs = frozenset(iterable)
fs = frozenset("abc")
print(fs, type(fs))

fs1 = set({"name": "张三", "age": 18})
print(fs1, type(fs1))

# 列表推导式
fs2 = frozenset(x ** 2 for x in range(1, 10) if x % 2 == 0)
print(fs2, type(fs2))

# 创建一个空的集合时，需要使用set{}或者frozenset{},直接花括号会认为为字典
# 集合中的元素都是不可变的，如果元素出现重复则会只取一个

# 利用集合将列表进行去重
l = [1, 2, 3, 3, 4]
s5 = set(l)
print(s5)
result = list(s5)
print(result, type(result))

# 单一集合操作
# 可变集合
# 增,增的内容为不可变的
s6 = {4, 5, 6}
s6.add(7)
print(s6, type(s6))

# 删除,指定元素不存在则返回错误,s.remove(element)
s6.remove(4)
print(s6)

# s.discard(element),删除指定的元素，没有指定元素时什么都不做
s6.discard(6)
print(s6)

# s.pop(),随机删除并返回集合中的元素，若集合为空，则返回一个错误
print(s.pop(), s)

# s.clear()，清空一个集合的所以元素
print(s.clear(), s)

# 查询
for r in s5:
    print(r, end="、")

print()

# 使用迭代器
its = iter(s5)
for r1 in its:
    print(r1, end="-")

print()

# 集合之间操作
# 交集：intersection(Iterable),字符串（只判定非数字）、列表、元组、字典（只判定key）、集合
# 可变集合与不可变集合求交集的时候，结果类型取.号左边的.集合本身并不改变
# intersection_update(...)，交集计算完毕后，会再次赋值给原对象，会更改原对象，所以只适用于可变集合
s7 = frozenset([1, 2, 3, 4, 5, 6])
s8 = {1, 4, 5, 8}
s9 = {1, 2, 3, 4, 5, 8}
# result1 = s7.intersection(s8)
# result1 = s7 & s8
# result1 = s8.intersection_update(s7)
# print(result1, type(result1), s8)
#
# # 并集
# # union()返回并集
# print(s7.union(s8), s7)
# # 逻辑或'|'返回并集
# print(s7 | s8, s7)
# # update()更新并集
# print(s8.update(s7), s8)

# 差集
# difference()、减号、difference_update()
rs = s9.difference(s8)
print(rs, s9)
# 属于s9不属于s8
print(s9 - s8)
# print(s8.difference_update(s9), s8)

# 判定：isdisjoint()两个集合不相交。issuperset()一个集合包含另一个集合。issubset()一个集合包含于另一个集合
print(s9.isdisjoint(s8))
print(s9.issuperset(s8))
print(s8.issubset(s9))





