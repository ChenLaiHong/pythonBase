import os
import matplotlib.image as img
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

##改变当前工作路径
os.chdir('E:\leaf-classification')
os.getcwd()

save_path = './kmeans_imgs'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

img_path = './images'
img_name_list = os.listdir(img_path)

# 对文件名称重新排序
img_name_list.sort(key=lambda x: int(x.split('.')[0]))
print(img_name_list)
train = pd.read_csv('train.csv')
Train_id = train['id']
Test = pd.read_csv('test.csv')
Test_id = Test['id']
Test.drop(['id'], inplace=True, axis=1)

## 把species转换为类标签。如把树叶名Acer_Opalus转为0
map_dic = {};
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

for _ in train.isna().sum():
    if _ != 0:
        print('存在缺失值')

X = train.drop(['Type'], axis=1)
y = train['Type']
print(y.head())
print("训练集尺寸:", X.shape)

## 划分训练集和测试集
from sklearn.model_selection import train_test_split

X1_train, X1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("训练集数据尺寸", X1_train.shape)
print("测试集数据尺寸", X1_test.shape)
print("训练集目标尺寸", y1_train.shape)
print("测试集目标尺寸", y1_test.shape)

rf_test = RandomForestClassifier()
rf_test.fit(X1_train, y1_train)
res = rf_test.predict(Test)
print("预测结果尺寸为:", res.shape)

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(res == i)[0].tolist()

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(y.values == i)[0].tolist()

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
            save_path = os.path.join(save_path, str(
            ))
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


# imagesclassifier(DImage, Train_id, Test_id, Train_label_dic, Test_label_dic, save_path)
