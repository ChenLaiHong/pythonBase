class Person:
    @classmethod
    def run(cls, a):
        print("这是一个类方法", cls, a)

# 通过类来调用
Person.run(123)

# 通过实例调用,传递的是实例对应的类
p = Person()
p.run(666)

func = Person.run
func(111)

# A是Person的子类
class A(Person):
    pass
# 原生类调用类方法，会把原生类本身传递给这个方法
A.run(223)