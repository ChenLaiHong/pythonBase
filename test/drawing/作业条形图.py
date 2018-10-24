import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()  # 加载机器学习的下的iris数据集,得到的是字典
iris_data = iris["data"]
# 存储sepal_length的数据
sepal_length = []
# 存储sepal_width的数据
sepal_width = []
# 存储petal_length的数据
petal_length = []
# 存储petal_width的数据
petal_width = []
# 循环150条数据，分别存起来
for i in iris_data:
    sepal_length.append(i[0])
    sepal_width.append(i[1])
    petal_length.append(i[2])
    petal_width.append(i[3])
# 为了能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 这里是petal_width的条形图，其他的直接在这里修改就可以了
plt.hist(petal_width, rwidth=0.9)
plt.xlabel("花瓣宽度")
plt.ylabel("计数")
plt.show()