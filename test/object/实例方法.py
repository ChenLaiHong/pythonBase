class Person:
    def eat(self, food):
        print("晚上吃", food, self)

# 标准调用
p = Person()
print(p)
# 不需要传递第一个参数，解析器自动把实例传到第一个参数
p.eat("土豆")

# 这里“青菜相当于一个实例”
func = Person.eat
func("青菜", "123")