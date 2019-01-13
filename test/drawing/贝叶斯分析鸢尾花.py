from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from matplotlib.colors import ListedColormap
muNB = GaussianNB()
iris = load_iris()
data = iris.data
target = iris.target
samples = data[:, :2]
muNB.fit(samples, target)
xmin, xmax = samples[:, 0].min(), samples[:, 0].max()
ymin, ymax = samples[:, 1].min(), samples[:, 1].max()
x = np.linspace(xmin, xmax, 300)
y = np.linspace(ymin, ymax, 300)
xx, yy = np.meshgrid(x, y)
X_test = np.c_[xx.ravel(), yy.ravel()]
y_ = muNB.predict(X_test)
colormap = ListedColormap(['#00aaff', '#aa00ff', '#ffaa00'])
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_)
plt.scatter(samples[:, 0], samples[:, 1], c=target, cmap=colormap)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_)
plt.scatter(samples[:, 0], samples[:, 1], c=target, cmap=colormap)
plt.show()
