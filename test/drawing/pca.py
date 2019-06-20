import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def loadDataSet(filename):
    with open(filename, 'r') as f:
        D = []
        for line in f.readlines():
            lineArr = line.strip().split('\t')
            smalldata = [float(num) for num in lineArr]
            D.append(smalldata)
        return D

D = loadDataSet('testSet.txt')

# 数据可视化
DMat = np.array(D)
plt.scatter(DMat[:, 0], DMat[:, 1])
sns.scatterplot(DMat[:, 0], DMat[:, 1], color='red')
plt.show()

# # 方差
# a = np.array([1, 2, 3, 4, 5])
# np.var(a)

# 1.取出矩阵均值
# mean_removed = DMat.mean(axis=0)
# # 2求出协方差矩阵X
# covMat = np.cov(mean_removed,rowvar=0)
# # 3.求出X的特征值和特征向量
# eigVals, eigVects = np.linalg.eig(covMat)
# print(eigVals)
# # 降维
# lowDimData = np.dot(mean_removed, eigVects[:, 1][:, np.newaxis])
# print(lowDimData)
# # 恢复高维
# reconstruct_data = np.dot(lowDimData, eigVects[:, 1][:, np.newaxis].T)+DMat.mean(axis=0)
# sns.scatterplot(DMat[:, 0], DMat[:, 1])
# sns.scatterplot(DMat[:, 0], DMat[:, 1], color='red')