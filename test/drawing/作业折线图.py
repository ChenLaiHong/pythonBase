import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()  # 加载机器学习的下的iris数据集，先来认识一下iris数据集的一些操作，其实iris数据集就是一个字典集。下面注释的操作，可以帮助理解
def change(data):
    for i in data:
        i[0], i[1] = i[1], i[0]
    return data

iris_setosa = iris.data[:50]  # 第一种花的数据
iris_versicolor = iris.data[50:100]  # 第二种花的数据
iris_virginica = iris.data[100:150]  # 第三种花的数据

# iris_setosa = change(iris_setosa)
# iris_versicolor = change(iris_versicolor)
# iris_virginica = change(iris_virginica)
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
x = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for i in iris_setosa:
    plt.plot(x,i,label = 'versicolor', c="g")
for i in iris_versicolor:
    plt.plot(x,i,label = 'versicolor', c="r")
for i in iris_virginica:
    plt.plot(x,i,label = 'versicolor', c="b")
plt.xlabel('value')
plt.ylabel('y_data')
plt.show()