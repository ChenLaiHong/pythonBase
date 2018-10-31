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
# 修改单个键值对，dic[key] = value,直接设置，如果key不存在，则新增，存在则修改
person3 = {"name": "王五", "age": 20}
print(person3)
person3["age"] = 18
print(person3)

# 批量修改键值对,根据新的字典，批量更新旧字典中的键值对
# 如果旧字典没有对应的Key,则新增键值对
# oldDic.update(newDic)
person3.update({"name": "王小五"})
print(person3)

# 根据key查找相应的值,key不存在会报错
print(person["name"])

# dic.get(key[default])如果不存在对应的key,则取给定的默认值default
# 如果没有默认值，则为None，不会报错，但是原字典不会新增这个键值对
print(person3.get("age"))
print(person3.get("age1", 666))

# dic.setdefault(key[,default])获取指定key对应的值
# 如果key不存在，则设置成指定默认值，并返回该值
# 如果默认值没给，则使用None代替
print(person3.setdefault("age"))
print(person3.setdefault("age1"), person3)

# 获取所有的值
print(person.values())
# 获取所有的键
print(person.keys())
# 获取字典的键值对
print(person.items())

# 遍历所有的key，根据指定的key获取到对应的值
d = {"name": "赵六", "age": 20, "address": "北京"}
# 获取所有的key
keys = d.keys()
for key in keys:
    print(d[key])

# 直接遍历所有的键值对
kvs = d.items()
for k, v in kvs:
    print(k, v)

# 计算键值对个数
print(len(d))

# 判定
# x in dic:判定dic中的key是否存在x
# x not in dic:判定dic中的key是否不存在x
print("age" in d)
print("age" not in d)

