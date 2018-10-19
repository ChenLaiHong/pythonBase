import matplotlib.pyplot as plt
# 设定x有值的地方
x = [1, 3, 5, 7, 9]
# 设定y有值的地方
y = [4, 6, 2, 8, 9]
# 画图
plt.bar(x, y)
# x的范围[0,12]，y的范围[0,10]
plt.axis([0, 12, 0, 10])
# 展示图
plt.show()