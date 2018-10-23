import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()  # 加载机器学习的下的iris数据集，先来认识一下iris数据集的一些操作，其实iris数据集就是一个字典集。下面注释的操作，可以帮助理解

iris_setosa = iris.data[:50]  # 第一种花的数据
iris_versicolor = iris.data[50:100]  # 第二种花的数据
iris_virginica = iris.data[100:150]  # 第三种花的数据

iris_setosa = np.hsplit(iris_setosa, 4)  # 运用numpy.hsplit水平分割获取各特征集合，分割成四列
iris_versicolor = np.hsplit(iris_versicolor, 4)
iris_virginica = np.hsplit(iris_virginica, 4)

setosa = {'sepal_length': iris_setosa[0], 'sepal_width': iris_setosa[1], 'petal_length': iris_setosa[2],
          'petal_width': iris_setosa[3]}

versicolor = {'sepal_length': iris_versicolor[0], 'sepal_width': iris_versicolor[1], 'petal_length': iris_versicolor[2],
              'petal_width': iris_versicolor[3]}

virginica = {'sepal_length': iris_virginica[0], 'sepal_width': iris_virginica[1], 'petal_length': iris_virginica[2],
             'petal_width': iris_virginica[3]}

temp = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
sepal_width_ticks = np.arange(2, 5, step=0.5)  # sepal_length分度值和刻度范围
sepal_length_ticks = np.arange(4, 8, step=0.5)  # sepal_width分度值和刻度范围
petal_width_ticks = np.arange(0, 2.5, step=0.5)  # petal_width分度值和刻度范围
petal_length_ticks = np.arange(1, 7, step=1)  # petal_length分度值和刻度范围

ticks = [sepal_length_ticks, sepal_width_ticks, petal_length_ticks, petal_width_ticks]

plt.figure(figsize=(12, 12))  # 设置画布大小

for i in range(0, 4):
    for j in range(0, 4):
        plt.subplot(4, 4, i * 4 + j + 1) # 创建子画布
        if i == j:
            print(i*4+j+1) #序列号
            plt.xticks([])
            plt.yticks([])
        else:
            plt.scatter(iris_setosa[j], iris_setosa[i], c='b', s=30, marker='x', alpha=0.5)
            plt.scatter(iris_versicolor[j], iris_versicolor[i], c='g', s=30, marker='+', alpha=0.5)
            plt.scatter(iris_virginica[j], iris_virginica[i], c='r', s=30, alpha=0.5)
            plt.xticks(ticks[j])
            plt.yticks(ticks[i])

plt.show()

# plt.savefig('iris.png', format='png')   #保存图片