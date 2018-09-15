class Person:
    # 类属性
    age = 2

    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.name)

    @classmethod
    def leifangfa(cls):
        print(cls)
        print(cls.age)
        # 类方法里面访问不了实例属性，这样写会报错
        # print(cls.name)

    @staticmethod
    def jingtaifangfa():
        # 这里拿不了对应的实例，也是访问不了实例属性
        print(Person.age)


p = Person()
# 实例属性
p.name = "张三"

# # 类属性访问
# print(Person.age)
# # 实例中没有相应属性时会去相应的类中找
# print(p.age)

# # 实例属性只能通过实例来访问
# print(p.name)

# 实例方法通过实例即可以访问类属性也可以访问实例属性
p.shilifangfa()

# 类方法通过类或者通过实例都是只能访问类属性，访问不了实例属性
p.leifangfa()

Person.jingtaifangfa()
