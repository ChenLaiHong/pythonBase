# 定义一个类,类名跟java的规则一样
# 经典类
class Person:
    pass

# Person的类名
print(Person.__name__)

print(Person)
# 根据这个类来实例化一个对象
p = Person()
print(p)

# 给对象动态添加属性
p.name = "张三"
p.age = 18
p.pets = ["小花", "小黑"]
# 打印当前对象的所有属性
print(p.__dict__)
# 打印类中所有属性,验证给对象添加的属性并没有给对应的类添加上
# 证明对象与类不是共用同一个空间的
print(Person.__dict__)

# 修改前的地址
print(p.pets, id(p.pets))
# 修改pets地址会改变
p.pets = [1, 2]
# 修改后的地址
print(p.pets, id(p.pets))

# 追加内容不改变地址
p.pets.append("小黄")
print(p.pets, id(p.pets))

