class Person:
    # 静态方法，没有默认参数
    @staticmethod
    def jingtai():
        print("这是一个静态方法")

# 可通过类调用也可通过实例调用
Person.jingtai()
p = Person()
p.jingtai()

func = Person.jingtai
func()