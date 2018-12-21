from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

iris_dataset = load_iris()  # 获取数据
# 对数据进行拆分，分为训练数据和测试数据
x_train, x_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)  # 获取KNN对象
knn.fit(x_train, y_train)  # 训练模型

# 评估模型
y_pre = knn.predict(x_test)
score = knn.score(x_test, y_test)  # 调用打分函数

if score > 0.9:
    x_new = np.array([[5, 2.9, 1, 0.3]])
    prediction = knn.predict(x_new)  # 预测
    # 可视化展示
    plt.title("KNN Classification")
    plt.plot(x_train, y_train, "b.")  # 训练数据打点
    plt.plot(x_test, y_test, "y.")  # 测试数据打点
    plt.plot(x_new, prediction, "ro")  # 预测数据打点
    plt.show()
else:
    print("used train or test data is not available !")