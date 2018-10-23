import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,5,7,8]

x1 = [1,2,3,4]
y1 = [5,9,12,14]

plt.plot(x,y,label = 'line one')
plt.plot(x1,y1,label = 'line two')
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.title('title is here!')
plt.legend()
plt.show()