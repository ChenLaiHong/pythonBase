# 方法的私有性
# 什么都不添加代表公有
# 在一个变量前面添加一个下划线代表受保护的属性
# 两个下划线代表私有属性

# 测试公有变量
# class Animal:
#     x = 10
#     # 类的内部访问
#     def test(self):
#         print(Animal.x)
#         print(self.x)
#     pass
#
# class Dog(Animal):
#     # 测试能不能继承这个公有变量
#     # 在原生类内部也能访问公有属性
#     def test2(self):
#         print(Dog.x)
#         print(self.x)
#     pass
#
# # 测试类的内部的方法
# a = Animal()
# a.test()
#
# d = Dog()
# d.test2()
#
# # 当前模块其他位置访问公有属性
# print(Animal.x)
# print(Dog.x)
#
# print(a.x)
# print(d.x)

# 测试其他模块能不能访问公有变量a,在TestFunction.py模块访问x
x = 666


