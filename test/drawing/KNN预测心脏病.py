# 读文件
import pandas as pd
import numpy as np
import random
from random import shuffle
import operator

df = pd.read_csv('heart.csv')

# 打乱数据，选择其中的70%作为训练集，剩余的30%作为测试集

random.seed(42)
indices = np.arange(0, (df.shape[0] - 1)).tolist()
train_num = int(0.7 * df.shape[0])
shuffle(indices)
train_indices = indices[:train_num]
test_indices = indices[train_num:]
train_data = df.iloc[train_indices, :]
test_data = df.iloc[test_indices, :]

## 训练集数据和标签
D = np.array(train_data.iloc[:, :-1])
L = np.array(train_data.iloc[:, -1]).astype(str)

## 测试集数据和标签
X = np.array(test_data.iloc[:, :-1])
Y = np.array(test_data.iloc[:, -1]).astype(str)

def knnClassifier(inX, D, L, k):
    'KNN算法分类器，inX未知数据，D，L分别是数据列表和标签列表'
    # 计算距离，并排序
    D = np.array(D);
    L = np.array(L)
    [m, n] = D.shape
    differMat = np.tile(inX, (m, 1)) - D
    distanceSqur = (differMat ** 2).sum(axis=1)
    distance = distanceSqur ** 0.5
    indices = np.argsort(distance)[:k]
    votelabels = L[indices]
    # 统计标签出现的次数
    count = {}
    for label in votelabels:
        count[label] = count.get(label, 0) + 1
    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    # print(count,res)
    return res[0][0]


def autoNorm(dataSet):
    '归一化'
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet


res = []
count = 0
for inX in X:
    res.append(knnClassifier(inX, D, L, 9))

for index, predict_label in enumerate(res):
    if predict_label == Y[index]:
        count += 1
print("KNN算法k=9时，准确率为%.2f" % (count / len(Y)))

##归一化特征之后准确率
res = [];
count = 0
for inX in autoNorm(X):
    res.append(knnClassifier(inX, autoNorm(D), L, 9))

for index, predict_label in enumerate(res):
    if predict_label == Y[index]:
        count += 1
print("归一化特征之后，KNN算法k=9时，准确率为%.2f" % (count / len(Y)))
