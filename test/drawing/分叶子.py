import os
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
##改变当前工作路径
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import NuSVC

os.chdir('E:\机器学习\树叶分类\树叶分类\leaf-classification')
save_path='E:\机器学习\树叶分类\树叶分类\leaf-classification\svc_images'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)
img_path='E:\机器学习\树叶分类\树叶分类\leaf-classification\images'
img_name_list=os.listdir(img_path)
#对文件名称重新排序
img_name_list.sort(key=lambda x: int(x.split('.')[0]))


train=pd.read_csv('train.csv')
Train_id=train['id']
Test=pd.read_csv('test.csv')
Test_id=Test['id']
Test.drop(['id'],inplace = True, axis = 1)

## 把species转换为类标签。如把树叶名Acer_Opalus转为0
map_dic={};i=-1
for _ in train['species']:
    if _ in map_dic:
        pass
    else:
        i+=1
        map_dic[_]=map_dic.get(_,i)
train['Type']=train['species'].map(map_dic)
#print(train['Type'])
train.drop(['species'],inplace = True, axis = 1)
train.drop(['id'],inplace = True, axis = 1)
corr = train.corr()
f, ax = plt.subplots(figsize=(25, 25))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5)
# plt.show()

for _ in train.isna().sum():
    if _!=0:
        print('存在缺失值')
X=train.drop(['Type'],axis=1)
y=train['Type']
print(y.head())
print("训练集尺寸:",X.shape)

## 划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=42 )
print("训练集数据尺寸",X_train.shape)
print("测试集数据尺寸",X_test.shape)
print("训练集目标尺寸",y_train.shape)
print("测试集目标尺寸",y_test.shape)

clf = NuSVC(probability=True)
clf.fit(X_train, y_train)


res=clf.predict(Test)
print("预测结果尺寸为:",res.shape)
Test_label_dic={}
for i in range(99):
    Test_label_dic[i]=np.where(res==i)[0].tolist()

Train_label_dic={}
for i in range(99):
    Train_label_dic[i]=np.where(y.values==i)[0].tolist()

print(Test_label_dic)

DImage=[]###建立所有图片的数据集
for img_name in img_name_list:
    img_full_path=os.path.join(img_path,img_name)
    DImage.append(img.imread(img_full_path))

train_val=Train_id.values[np.array(Train_label_dic[i])]-1
test_val=Test_id.values[np.array(Test_label_dic[i])]-1
Train_imgs=np.array(DImage)[train_val]
Test_imgs=np.array(DImage)[test_val]

def imagesclassifier(DImage,Train_id,Test_id,Train_label_dic,Test_label_dic,root_path):
    '''DImage为图像数据集(循环读取的1584张图片)，Train_id,Test_id分别是train.csv
    和test.csv 内id列，Train_label_dic,Test_label_dic是树叶类别标签和图片索引对应关系'''
    if os.path.exists(root_path) is False:
        os.makedirs(root_path)
    save_path=root_path
    for i in range(99):
        j=0
        train_val=Train_id.values[np.array(Train_label_dic[i])]-1
        test_val=Test_id.values[np.array(Test_label_dic[i])]-1
        Train_imgs=np.array(DImage)[train_val]
        Test_imgs=np.array(DImage)[test_val]

        for index,_ in enumerate(Train_imgs):
            img_name='train'+str(train_val[index])+'.jpg'
            save_path=os.path.join(save_path,str(i))
            if os.path.exists(save_path) is False:
                os.makedirs(save_path)
            img.imsave(os.path.join(save_path,img_name),_,cmap='binary')
            save_path=root_path
            j+=1

        for index,_ in enumerate(Test_imgs):
            img_name='test'+str(test_val[index])+'.jpg'
            save_path=os.path.join(save_path,str(i))
            if os.path.exists(save_path) is False:
                os.makedirs(save_path)
            img.imsave(os.path.join(save_path,img_name),_,cmap='binary')
            save_path=root_path
            j+=1

imagesclassifier(DImage,Train_id,Test_id,Train_label_dic,Test_label_dic,save_path)

