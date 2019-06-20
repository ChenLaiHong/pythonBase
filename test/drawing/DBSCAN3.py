import pandas as pd
import numpy as np
# 读入第三方包
from sklearn import preprocessing
# 选取建模的变量
from sklearn.cluster import DBSCAN
train=pd.read_csv('E:\\leaf-classification\\train.csv',index_col='id')
Test=pd.read_csv('E:\\leaf-classification\\test.csv',index_col='id')

train.drop(['species'],inplace = True, axis = 1)
train_data = train.iloc[ :, :]
test_data =Test.iloc[:,:]

frames = [train, Test]
result = pd.concat(frames)
data2= 1.0*(result - result.mean())/result.std() #数据标准化  #z-score标准化法 z-score 标准化(zero-mean normalization)也叫标准差标准化，经过处理的数据符合标准正态分布，即均值为0，标准差为1
X=data2[data2.columns[:]].as_matrix()



# 构建空列表，用于保存不同参数组合下的结果
res = []
# 迭代不同的eps值
for eps in np.arange(0.001,1,0.05):
    # 迭代不同的min_samples值
    for min_samples in range(2,10):
        dbscan = DBSCAN(eps = eps, min_samples = min_samples)
        # 模型拟合
        dbscan.fit(X)
        # 统计各参数组合下的聚类个数（-1表示异常点）
        n_clusters = len([i for i in set(dbscan.labels_) if i != -1])
        # 异常点的个数
        outliners = np.sum(np.where(dbscan.labels_ == -1, 1,0))
        # 统计每个簇的样本个数
        stats = str(pd.Series([i for i in dbscan.labels_ if i != -1]).value_counts().values)
        res.append({'eps':eps,'min_samples':min_samples,'n_clusters':n_clusters,'outliners':outliners,'stats':stats})
# 将迭代后的结果存储到数据框中
df = pd.DataFrame(res)
print(df)
# 根据条件筛选合理的参数组合
df.loc[df.n_clusters == 3, :]

