import matplotlib.pyplot as plt

label = 'A','B','C','D'
size = [12,30,45,10]
fig,ax = plt.subplots()
explode = (0,0.1,0,0)
ax.pie(size,labels = label,autopct = '%1.1f%%',shadow = True,startangle = 90,explode=explode)
ax.axis('equal')

plt.show()