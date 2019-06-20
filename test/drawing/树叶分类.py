import os
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## 改变当前工作路径
os.chdir('E:\机器学习\树叶分类\树叶分类\leaf-classification')
# 存放99个文件夹，存放99种树叶
save_path = './filtered_imgs'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)
img_path = './images'
img_name_list = os.listdir(img_path)
# 对文件名称重新排序
img_name_list.sort(key=lambda x: int(x.split('.')[0]))
# 顺序读取前12张图片并排序
DImage = []
for img_name in img_name_list[:12]:
    img_full_path = os.path.join(img_path, img_name)
    DImage.append(img.imread(img_full_path))
##可视化树叶图片
f = plt.figure(figsize=(15, 15))
for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.axis("off")
    plt.title("image_ID:{0}".format(img_name_list[i].split('.jpg')[0]))
    plt.imshow(DImage[i], cmap='hot')
plt.show()
train = pd.read_csv('train.csv')
Train_id = train['id']
Test = pd.read_csv('test.csv')
Test_id = Test['id']
Test.drop(['id'], inplace=True, axis=1)
print("树叶种类数目为：", len(set(train['species'])))
## 把species转换为类标签。如把树叶名Acer_Opalus转为0
map_dic = {}
i = -1
for _ in train['species']:
    if _ in map_dic:
        pass
    else:
        i += 1
        map_dic[_] = map_dic.get(_, i)
train['Type'] = train['species'].map(map_dic)
# print(train['Type'])
train.drop(['species'], inplace=True, axis=1)
train.drop(['id'], inplace=True, axis=1)
corr = train.corr()
f, ax = plt.subplots(figsize=(25, 25))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5)
plt.show()
for _ in train.isna().sum():
    if _ != 0:
        print('存在缺失值')
X = train.drop(['Type'], axis=1)
print(X, "X里面是什么？==========================")
y = train['Type']
print(y.head())
print("训练集尺寸:", X.shape)
## 划分训练集和测试集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=42)
print("训练集数据尺寸", X_train.shape)
print("测试集数据尺寸", X_test.shape)
print("训练集目标尺寸", y_train.shape)
print("测试集目标尺寸", y_test.shape)
## 数据特征一共有196个，可用PCA 变换对数据降维

# 使用单位方差标准化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

# 协方差矩阵的特征分解，计算数据集协方差矩阵的特征对。
# cov函数得到标准化处理的训练集协方差矩阵
# eig函数进行特征分解，得到特征向量及其对应的特征值。
cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
print('\nEigenvalues \n%s' % eigen_vals)

## 此处完成PCA coding
## 此处完成PCA coding
## 此处完成PCA coding
## 归一化 coding

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

clf = KNeighborsClassifier(3)
clf.fit(X_train, y_train)
print("*" * 30)
print('KNeighborsClassifier')
print('=========结果=========')
train_predictions = clf.predict(X_test)
acc = accuracy_score(y_test, train_predictions)
print("Accuracy: {:.4%}".format(acc))
print("=" * 30)
res = clf.predict(Test)
print(res, "*"*50)
print("预测结果尺寸为:", res.shape)

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(res == i)[0].tolist()

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(y.values == i)[0].tolist()

###Train_label_dic[0]=[0, 180, 568, 633, 702, 720, 791, 821, 903, 934]
###表示训练集表内，类别种类为0的树叶对应索引为[0, 180, 568, 633, 702, 720, 791, 821, 903, 934]
DImage = []  ###建立所有图片的数据集
for img_name in img_name_list:
    img_full_path = os.path.join(img_path, img_name)
    DImage.append(img.imread(img_full_path))


def imagesclassifier(DImage, Train_id, Test_id, Train_label_dic, Test_label_dic, root_path):
    '''DImage为图像数据集(循环读取的1584张图片)，Train_id,Test_id分别是train.csv
    和test.csv 内id列，Train_label_dic,Test_label_dic是树叶类别标签和图片索引对应关系'''
    if os.path.exists(root_path) is False:
        os.makedirs(root_path)
    save_path = root_path
    for i in range(99):
        j = 0
        train_val = Train_id.values[np.array(Train_label_dic[i])] - 1
        test_val = Test_id.values[np.array(Test_label_dic[i])] - 1
        Train_imgs = np.array(DImage)[train_val]
        Test_imgs = np.array(DImage)[test_val]
        for index, _ in enumerate(Train_imgs):
            img_name = 'train' + str(train_val[index]) + '.jpg'
            save_path = os.path.join(save_path, str(i))
            if os.path.exists(save_path) is False:
                os.makedirs(save_path)
            img.imsave(os.path.join(save_path, img_name), _, cmap='binary')
            save_path = root_path
            j += 1

        for index, _ in enumerate(Test_imgs):
            img_name = 'test' + str(test_val[index]) + '.jpg'
            save_path = os.path.join(save_path, str(i))
            if os.path.exists(save_path) is False:
                os.makedirs(save_path)
            img.imsave(os.path.join(save_path, img_name), _, cmap='binary')
            save_path = root_path
            j += 1


imagesclassifier(DImage, Train_id, Test_id, Train_label_dic, Test_label_dic, save_path)
