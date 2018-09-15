# python中万物皆对象，类对象也是有相应的类的
# 元类：创建类对象的类
# 相当于java中的所有类都是Object类的子类
num = 1
# num对应的类是int
print(num.__class__)
# int 对应的类是type（这里type就是元类）
print(int.__class__)

name = "张三"
# name对应的类是str
print(name.__class__)
# str 对应的类是type（这里type就是元类）
print(str.__class__)

class Person:
    def run(self, distance, step):
        """
        这个方法的作用效果
        :param distance: 距离
        :param step: 步长
        :return: 
        """
        return distance * step
    pass

p = Person()
print(p.__class__)
print(Person.__class__)
print(p.run(5, 3))