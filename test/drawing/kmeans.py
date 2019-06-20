import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, :4]  # #表示我们取特征空间中的4个维度
print(X.shape)
print(X)

estimator = KMeans(n_clusters=3)  # 构造聚类器
estimator.fit(X)  # 聚类
print(type(estimator),"="*50)
label_pred = estimator.labels_  # 获取聚类标签
print(label_pred,"="*50)
# 绘制k-means结果
x0 = X[label_pred == 0]

x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()