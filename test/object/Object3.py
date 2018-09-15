# 方法相关，方法和函数调用方式不同
# 方法调用要通过对象，函数直接就能调用
# 定义函数
def sum(i, j):
    print(i + j)

sum(1, 5)

# 定义方法
class Person:
    # 实例方法默认第一个参数是一个实例，self是实例
    def eat(self):
        print("这是一个实例方法", self)

    # 类方法默认第一个参数是一个类
    @classmethod
    def leifangfa(cls):
        print("这是一个类方法", cls)

    # 静态方法不作要求
    @staticmethod
    def jingtaifangfa():
        print("这是一个静态方法")

p = Person()
p.eat()

Person.jingtaifangfa()
Person.leifangfa()
p.jingtaifangfa()

# 方法都是存放到类里面，存放到字典里
print(Person.__dict__)


