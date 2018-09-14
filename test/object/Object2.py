# 类属性
class Person:
    address = "浙江"


Person.name = "李四"
Person.age = 19

print(Person.__dict__)

# 对象可以访问到类的属性
p = Person()
p.age = 25
print(p.name)
# 类与对象都有相同的属性就会先从对象中找
print(p.age)