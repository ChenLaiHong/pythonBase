import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()  # 加载机器学习的下的iris数据集,得到的是字典
iris_data = iris["data"]
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
for i in iris_data:
    sepal_length.append(i[0])
    sepal_width.append(i[1])
    petal_length.append(i[2])
    petal_width.append(i[3])
# 为了能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.hist(petal_width, rwidth=0.9)

plt.xlabel("花瓣宽度")
plt.ylabel("计数")
plt.show()