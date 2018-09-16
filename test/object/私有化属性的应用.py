class Person:
    # 主要作用，当我们创建好一个实例对象之后，会自动调用这个方法，来初始化这个对象
    def __init__(self):
        self.__age = 18

    def setAge(self, value):
        # 判定前面一个对象是否是某个类型
        if isinstance(value, int) and 0 < value < 200:
            self.__age = value
        else:
            print("输入数据有问题，请重新输入")
    def getAge(self):
        return self.__age

p = Person()
p.setAge(20)
print(p.getAge())


# 注意：在变量或属性后面添加一个下划线主要是为了跟关键字区分
# 左右各添加两个下划线一般都是系统的内置的，避免这样的命名