# 方法的私有性
# 什么都不添加代表公有：
# 类的内部、子类的内部、模块其他位置、跨模块都能正常访问

# 在一个变量前面添加一个下划线代表受保护的属性
# 类内部、子类内部正常访问；模块内其他位置、跨模块访问会有警告

# 两个下划线代表私有属性
# 类内部可以访问，子类内部、模块内其他位置不能访问，跨模块看情况

# 测试公有变量、受保护变量
# class Animal:
#     x = 10
#     _y = 233
#     # 类的内部访问
#     def test(self):
#         print(Animal.x)
#         print(self.x)
#         print(Animal._y)
#         print(self._y)
#     pass
#
# class Dog(Animal):
#     # 测试能不能继承这个公有变量
#     # 在原生类内部也能访问公有属性
#     def test2(self):
#         print(Dog.x)
#         print(self.x)
#         print(Dog._y)
#         print(self._y)
#     pass
#
# # 测试类的内部的方法
# a = Animal()
# a.test()
#
# d = Dog()
# d.test2()
#
# # 当前模块其他位置访问
# print(Animal.x)
# print(Dog.x)
#
# print(Animal._y)
# print(Dog._y)
#
# print(a.x)
# print(d.x)
#
# print(a._y)
# print(d._y)

# # 测试其他模块能不能访问公有变量a,在TestFunction.py模块访问x
__all__ = ["_y", "x", "__k"]
x = 666
_y = 233
__k = 555


# 私有属性

class Animal:
    __x = 100
    # 类的内部访问
    def test(self):
        print(Animal.__x)
        print(self.__x)
    pass

class Dog(Animal):
    # 测试能不能继承这个私有变量
    def test2(self):
        print(Dog.__x)
        print(self.__x)
    pass

# # 测试类的内部的方法
a = Animal()
# a.test()

d = Dog()
# d.test2()

# 当前模块其他位置访问
# print(Animal.__x)
# print(Dog.__x)
# print(Animal.__x)
# print(Dog.__x)

# 这样可以访问私有属性，但尽量不要这样访问
print(Animal._Animal__x)