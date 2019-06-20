from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score
import numpy as np
import pandas as pd
train=pd.read_csv('E:\\leaf-classification\\train.csv')
# Test=pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\test.csv')


train_data = train.iloc[ :, 2:]
# print(train_data)
train_data = np.array(train_data)
# print(train_data)
# print(len(train_data))
## 把species转换为类标签。如把树叶名Acer_Opalus转为0
map_dic={};i=-1
for _ in train['species']:
    if _ in map_dic:
        pass
    else:
        i+=1
        map_dic[_]=map_dic.get(_,i)

train['Type']=train['species'].map(map_dic)
# train.head()

train_label = np.array(train.iloc[:,-1])
# print(train_label)


from sklearn.model_selection import train_test_split
# # 划分数据集train_test_split() 第一个参数表示特征值，第二个参数表示目标值，test_size表示测试集所占的百分比(推荐0.25)
x_train, x_test, y_train, y_test = train_test_split(train_data, train_label, test_size=0.2)  # 划分是按比例随机划分
# 返回值 x_train表示训练集的特征值，x_test表示测试集的特征值，y_train表示训练集的目标值，y_test表示测试集的目标值


def pca(D,numfeat):
    DMat=np.array(D)
    mean_removed=DMat-DMat.mean(axis=0)
    DCovMat=np.cov(mean_removed,rowvar=0)
    eigval,eigvec=np.linalg.eig(DCovMat)
    ###选择特征值前numfeat大的特征向量索引
    tar_index=np.argsort(eigval)[:-(numfeat+1):-1]
    ##选取的特征向量
    reduced_vec=eigvec[:,tar_index]
    lowDataSet=np.dot(mean_removed,reduced_vec)
    reconstructMat=np.dot(lowDataSet,
                          reduced_vec.T)+DMat.mean(axis=0)
    #print(reconstructMat.shape)
    return lowDataSet,reconstructMat

lowDataSet,reconstructMat = pca(train_data, 180)
X_train, X_test, Y_train, Y_test = train_test_split(lowDataSet, train_label, test_size=0.2)  # 划分是按比例随机划分

from xgboost import XGBClassifier
XGBClassifier = XGBClassifier()
learning_rate = [0.0001,0.001,0.01,0.1,0.2,0.3] #学习率
gamma = [1, 0.1, 0.01, 0.001]
param_grid = dict(learning_rate = learning_rate,gamma = gamma)#转化为字典格式，网络搜索要求
cv = StratifiedShuffleSplit(n_splits=10,test_size=0.2,random_state=15)#将训练/测试数据集划分10个互斥子集，
grid_search = GridSearchCV(XGBClassifier,param_grid,n_jobs = -1,cv = cv)

grid_search.fit(x_train,y_train)
# rf_grid = grid_search.best_estimator_
# print(rf_grid.score(x_train,y_train))
# print(rf_grid.score(x_test,y_test))