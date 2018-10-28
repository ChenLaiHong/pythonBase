import pandas as pd
import matplotlib.pyplot as plt

data = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
dataset = pd.read_csv(data, names=names)
title = ["Iris", "Iris-setosa", "Iris-versicolor", "Iris-virginica"]
dataList = [dataset, dataset[:50], dataset[50:100], dataset[100:150]]
for i in range(1, 5):
    plt.figure(i)
    dataList[i-1].plot(kind='box')
    plt.title(title[i-1])
    plt.ylabel("values(centermeters")

plt.show()
