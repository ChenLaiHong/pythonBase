import pandas as pd
import numpy as np
import random
from random import shuffle
from sklearn.tree import DecisionTreeClassifier

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

# 训练
clf = DecisionTreeClassifier()
# 注意均使用训练数据集和样本类标
clf.fit(D, L)
# print(clf)

# 预测结果
predict_target = clf.predict(X)

count = 0
for index, predict_label in enumerate(predict_target):
    if predict_label == Y[index]:
        count += 1
print("准确率为%.2f" % (count / len(Y)))

