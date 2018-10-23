# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:17:37 2018

@author: 吴铭明
"""

import pandas as pd
import matplotlib.pyplot as plt

data = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']



dataset = pd.read_csv(data, names=names)
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# dataset[:50].plot(kind='box')


# dataset.boxplot()

plt.figure(1) 
dataset.plot(kind='box')
plt.title("Iris")
plt.ylabel("values(centermeters")

plt.figure(2) 
dataset[:50].plot(kind='box')
plt.title("Iris-setosa")
plt.ylabel("values(centermeters")

plt.figure(3) 
dataset[50:100].plot(kind='box')
plt.title("Iris-versicolor")
plt.ylabel("values(centermeters")

plt.figure(4) 
dataset[100:150].plot(kind='box')
plt.title("Iris-virginica")
plt.ylabel("values(centermeters")






plt.show()
