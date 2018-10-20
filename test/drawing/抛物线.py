import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = x**2

x1 = [1,2,3,4]
y1 = [1,21,3,4]
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()