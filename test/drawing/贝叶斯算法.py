# 计算训练数据集数据中各属性在各类中的概率
def calculae(train):
    """
    :type train: 原始训练集
    """
    # 存放每种属性的个数，键是对应的属性，值是个数
    # 在遍历列表的时候最后的一个值都是表示是否购买电脑，0代表购买，1代表不购买
    leibie = ["年龄：","收入：","学生：","信誉："]
    buy_result = {}
    notbuy_result = {}
    # buy_count: 整个训练集中会购买电脑的个数
    # notbuy_count：整个训练集中不会购买电脑的个数
    buy_count,notbuy_count = 0, 0
    train_samples = [sample.split(' ') for sample in train]
    for i in range(len(train_samples[0])-1):
        for j in range(len(train_samples)):
            train_samples[j][i] = leibie[i]+train_samples[j][i]
    for i in train_samples:
        # 代表是购买电脑
        if i[len(i)-1] == "是":
            buy_count += 1
            for j in range(len(i)-1):
                if i[j] in buy_result:
                    buy_result[i[j]] += 1
                else:
                    buy_result[i[j]] = 1
        else:
            notbuy_count += 1
            for j in range(len(i)-1):
                if i[j] in notbuy_result:
                    notbuy_result[i[j]] += 1
                else:
                    notbuy_result[i[j]] = 1
    for i in buy_result:
        print("在购买电脑的情况下",i,"的概率为：","%0.3f" %(buy_result[i]/buy_count))
    for i in notbuy_result:
        print("在不购买电脑的情况下",i,"的概率为：",notbuy_result[i]/notbuy_count)

# 描述属性分别用数字替换
# 年龄, <=30-->0, 31~40-->1, >40-->2
# 收入, '低'-->0, '中'-->1, '高'-->2
# 是否学生, '是'-->0, '否'-->1
# 信誉: '中'-->0, '优'-->1
# 类别属性用数字替换
# 购买电脑是-->0, 不购买电脑否-->1
MAP = [{'<=30': 0, '31~40': 1, '>40': 2},
       {'低': 0, '中': 1, '高': 2},
       {'是': 0, '否': 1},
       {'中': 0, '优': 1},
       {'是': 0, '否': 1}]

# 训练样本
train_samples = ["<=30 高 否 中 否",
                 "<=30 高 否 优 否",
                 "31~40 高 否 中 是",
                 ">40 中 否 中 是",
                 ">40 低 是 中 是",
                 ">40 低 是 优 否",
                 "31~40 低 是 优 是",
                 "<=30 中 否 中 否",
                 "<=30 低 是 中 是",
                 ">40 中 是 中 是",
                 "<=30 中 是 优 是",
                 "31~40 中 否 优 是",
                 "31~40 高 是 中 是",
                 ">40 中 否 优 否"]

calculae(train_samples)
# 测试样本
test = ["<=30 中 是 中", "31~40 中 否 优", ">40 中 否 优"]

# 下面步骤将文字，转化为对应数字
train_samples = [sample.split(' ') for sample in train_samples]
for j in range(len(train_samples[0])):
        for k in range(len(train_samples)):
            train_samples[k][j] = MAP[j][train_samples[k][j]]
print(train_samples)

# 训练样本数量
n_sample = len(train_samples)

# 计算每个属性有哪些取值
attr = []
for i in range(0, len(train_samples[0])):
    attr.append([])
for sample in train_samples:
    for i in range(0, len(train_samples[0])):
        if sample[i] not in attr[i]:
            attr[i].append(sample[i])

# 每个属性取值的个数
n_attr = [len(attr) for attr in attr]

# 初始化不同类别的样本个数
n_c = [0]*2

# 计算不同类别的样本个数
for sample in train_samples:
    n_c[sample[len(train_samples[0])-1]] += 1
print("购买电脑的个数：", n_c[0], "不购买电脑的个数：", n_c[1])
# 计算不同类别样本所占概率
p_c = [n_cx / sum(n_c) for n_cx in n_c]
print("购买电脑的概率：", p_c[0], "不购买电脑的概率：", p_c[1])

# 将用户按照类别分类
# 字典中键为1则表示不购买电脑，0则购买，值是矩阵形式对应的是各属性的值
samples_at_c = {}
for c in attr[len(train_samples[0])-1]:
    samples_at_c[c] = []
for sample in train_samples:
    samples_at_c[sample[len(train_samples[0])-1]].append(sample)
# print(samples_at_c)

for i in test:
    temp_X = i
    X = i.split(' ')
    for j in range(len(X)):
            X[j] = MAP[j][X[j]]
    # 记录 每个类别的训练样本中，取待分类样本的某个属性值的样本个数
    n_attr_X = {}
    for c in attr[len(train_samples[0])-1]:
        n_attr_X[c] = []
        for j in range(0, len(train_samples[0])-1):
            n_attr_X[c].append(0)

    # 计算 每个类别的训练样本中，取待分类样本的某个属性值的样本个数
    for c, samples_at_cx in zip(samples_at_c.keys(), samples_at_c.values()):
        for sample in samples_at_cx:
            for i in range(0, len(train_samples[0])-1):
                if X[i] == sample[i]:
                    n_attr_X[c][i] += 1

    # 字典转化为list
    n_attr_X = list(n_attr_X.values())
    # 位置交换一下，下面105行概率计算要对应
    n_attr_X[0], n_attr_X[1] = n_attr_X[1], n_attr_X[0]
    # 交换后就是买电脑的各个属性的个数在前，不买的在后
    # print(n_attr_X)

    # 存储最终的概率
    result_p = []
    for i in range(0, n_attr[len(train_samples[0])-1]):
        result_p.append(p_c[i])

    # 计算概率
    for i in range(0, n_attr[len(train_samples[0])-1]):
        n_attr_X[i] = [x/n_c[i] for x in n_attr_X[i]]
        for x in n_attr_X[i]:
            result_p[i] *= x
    print("当待分类样本是（", temp_X, "）时", "买电脑的概率是：", result_p[0], "不买电脑的概率是：", result_p[1])

    # 找到概率最大对应的那个类别，就是预测样本的分类情况
    predict_class = result_p.index(max(result_p))
    if predict_class == 0:
        print("所以当待分类样本为( %s )时，很大的概率是买电脑" % (temp_X))
    else:
        print("所以当待分类样本为( %s )时，很大的概率是不买电脑" % (temp_X))
