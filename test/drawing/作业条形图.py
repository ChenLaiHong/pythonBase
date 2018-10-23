import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()  # 加载机器学习的下的iris数据集，先来认识一下iris数据集的一些操作，其实iris数据集就是一个字典集。下面注释的操作，可以帮助理解
iris_data = iris["data"]
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
for i in iris_data:
    print(i)
    sepal_length.append(i[0])
    sepal_width.append(i[1])
    petal_length.append(i[2])
    petal_width.append(i[3])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.hist(petal_width, rwidth=0.9)

plt.xlabel("花瓣宽度")
plt.ylabel("计数")
plt.show()