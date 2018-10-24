import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()  # 加载机器学习的下的iris数据集，
# 交换顺序
def change(data):
    for i in data:
        i[0], i[1] = i[1], i[0]
    return data

iris_setosa = iris.data[:50]  # 第一种花的数据
iris_versicolor = iris.data[50:100]  # 第二种花的数据
iris_virginica = iris.data[100:150]  # 第三种花的数据
# 第二幅图使用
iris_setosa = change(iris_setosa)
iris_versicolor = change(iris_versicolor)
iris_virginica = change(iris_virginica)
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
# x坐标的值
x = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for i in iris_setosa:
    plt.plot(i, c="g",ls= '--', alpha=0.3)

for i in iris_versicolor:
    plt.plot(i, c="r",ls='-.', alpha=0.3)

for i in iris_virginica:
    plt.plot(x, i, c="b",ls='-', alpha=0.3)

plt.xlabel('value')
plt.show()