import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

data = load_iris() #完成数据的导入
m = data['data']
# 将其与m数组形成对应关系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in m:
    x = i[0]
    y = i[1]
    z = i[3]
    #此处dx，dy，dz是决定在3D柱形图中的柱形的长宽高三个变量
    dx = 0.3 * np.ones_like(x)
    dy = 0.3 * np.ones_like(y)
    dz = abs(z) * z.flatten()
    dz = dz.flatten() / abs(z)
    z = np.zeros_like(z)
    #设置三个维度的标签
    ax.set_xlabel('sepal_length')
    ax.set_ylabel('sepal_width')
    ax.set_zlabel('petal_width')
    ax.bar3d(x, y, z, dx, dy, dz, zsort='average')
plt.show()
