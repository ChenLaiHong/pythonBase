import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(1,100,100)
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(x,bins,rwidth=0.8)
plt.show()
