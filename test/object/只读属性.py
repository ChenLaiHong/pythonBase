class Person(object):
    # 主要作用，当我们创建好一个实例对象之后，会自动调用这个方法，来初始化这个对象
    def __init__(self):
        self.__age = 18

    # 主要作用就是可以以使用属性的方式来使用这个方法
    @property
    def age(self):
        return self.__age

p = Person()
print(p.age)