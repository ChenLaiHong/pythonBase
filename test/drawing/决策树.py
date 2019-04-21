# 导入数据集iris
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
# 导入决策树DTC包
from sklearn.tree import DecisionTreeClassifier
# 输出准确率 召回率 F值
from sklearn import metrics

# 载入数据集
iris = load_iris()

# 训练集
train_data = np.concatenate((iris.data[0:40, :], iris.data[50:90, :], iris.data[100:140, :]), axis=0)
# 训练集样本类别
train_target = np.concatenate((iris.target[0:40], iris.target[50:90], iris.target[100:140]), axis=0)
# 测试集
test_data = np.concatenate((iris.data[40:50, :], iris.data[90:100, :], iris.data[140:150, :]), axis=0)
# 测试集样本类别
test_target = np.concatenate((iris.target[40:50], iris.target[90:100], iris.target[140:150]), axis=0)

print("训练集", train_target)
# 训练
clf = DecisionTreeClassifier()
# 注意均使用训练数据集和样本类标
clf.fit(train_data, train_target)
print(clf)

# 预测结果
predict_target = clf.predict(test_data)
print(predict_target)

# 预测结果与真实结果比对
print(sum(predict_target == test_target),"==========================")

print(metrics.classification_report(test_target, predict_target))
print(metrics.confusion_matrix(test_target, predict_target))

# 获取花卉测试数据集两列数据集
X = test_data
L1 = [n[0] for n in X]
print(L1)
L2 = [n[1] for n in X]
print(L2)

# 绘图
# plt.scatter(L1, L2, c=predict_target, marker='x')  # cmap=plt.cm.Paired
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.title("决策树算法")
# plt.show()
