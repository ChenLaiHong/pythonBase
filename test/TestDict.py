# 字典：无序的，可变的键值对集合
# key不能重复，重复了后面的就会覆盖前面的,key为任意不可变类型
person = {"name": "zs", "age": 18, "heigth": 178}
print(person, type(person))

# 调用静态方法生成字典,dict.fromkeys(key, value)
person1 = dict.fromkeys("123", 666)
print(person1)

# 增加dic[key] = value
person["address"] = "上海"
print(person)

# 删除
# del dic[key],当key不存在会报错
del person["heigth"]
print(person)

# dic.pop(key[,default]),删除指定的键值对，并返回对应的值
# 如果key不存在，直接返回给定的default值,default不写key又不存在则会报错

# result = person.pop("age")
# print(result, person)
result1 = person.pop("age1", 666)
print(result1, person)

# dic.popitem()一般删除末尾键值对，并以元组的形式返回该键值对
# 如果字典为空，则报错
person2 = {"name": "lisi", "age": 28, "weigh": 178}
result2 = person2.popitem()
print(result2, person2)

# dic.clear()删除字典内所有键值对，返回None
# 注意字典对象本身还存在，只不过内容被清空，注意和del区别
# del是直接所有删除
person2.clear()
print(person2)
# 只改值不能改key
# 根据key查找相应的值
print(person["name"])
