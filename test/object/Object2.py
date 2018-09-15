# 类属性,各个对象共享类属性
# class Person:
#     address = "浙江"
#
#
# Person.name = "李四"
# Person.age = 19
#
# print(Person.__dict__)
#
# # 注意：给类新增或者修改属性，不能通过对象去修改，只能是类名.属性
# # 对象可以访问到类的属性
# p = Person()
# p.age = 25
# print(p.name)
# print(p.__dict__)
# # 类与对象都有相同的属性就会先从对象中找
# print(p.age)
#
# # 对象中的__dict__属性能直接被修改，类中的只能读
# p.__dict__ = {"age": 36}
# print(p.__dict__, p.age)

# 在类里面限定对象能添加的属性
class Person:
    __slots__ = ["name", "age", "address", "phone"]


p = Person()
p.age = 18
print(p.age)
