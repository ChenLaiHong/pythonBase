# 将数据进行分季节
def jijie(data_list):
    result = {}
    temp = []
    count = 1
# 按时间顺序从最早时间开始找，每13条数据一个季节
    for i in range(len(data_list)-1, 0, -13):
        for j in range(i, i-13, -1):
            linshi = data_list[j]
            # 要去掉每行字符串最后的换行符
            temp.append(linshi.strip())
        result[count] = temp
        temp = []
        count += 1
    return result

# 将每个季节的Adj Close的值取出来，然后拿最大的值减最小的值得到差值存到字典
def find(datas_dict):
    result = {}
    flag = []
    for i in datas_dict:
        temp = datas_dict[i]
        for j in temp:
            temp_list = j.split(",")
            flag.append(float(temp_list[-1]))
        bigger = max(flag)
        small = min(flag)
        result[i] = float('%0.2f' % (bigger - small))
        flag = []
    return result

# 此方法用于第3、4问
# 每一个季度中第一周的open值减去第13周的Close值，得到该季度的变化值作为值放到字典中
def jueduizhi(datas_dict):
    result = {}
    for i in datas_dict:
        # 第一周Open的值
        temp = datas_dict[i]
        one = temp[0].split(",")
        diyi = float(one[1])
        # 第十三周Close的值
        three = temp[-1].split(",")
        dishisan = float(three[4])
        result[i] = float('%0.2f' % (diyi - dishisan))
    return result

datas = open("StandardPoors500-week-20141018.csv")
lines = datas.readlines()
# 去除第一行
lines = lines[1:]
# 将数据按每13条一个季节
result_dict = jijie(lines)

# 第1、2问
# result_chazhi = find(result_dict)
# # 排序后的结果，从小到大
# result_pai = sorted(result_chazhi.items(), key=lambda n: n[1])

# # 差值最大的
# result = result_pai[-1]
# temp = result_dict[result[0]]
# temp_start = temp[0]
# temp_end = temp[-1]
# start, end = temp_start.split(","), temp_end.split(",")
# print("该季节起始日期：", start[0])
# print("该季节结束日期：", end[0])
# print("最大差值：", result[1])


# 差值最小的
# result = result_pai[0]
# temp = result_dict[result[0]]
# temp_start = temp[0]
# temp_end = temp[-1]
# start, end = temp_start.split(","), temp_end.split(",")
# print("该季节起始日期：", start[0])
# print("该季节结束日期：", end[0])
# print("最小差值：", result[1])

# 第3、4问
result = jueduizhi(result_dict)
result_jueduizhi = sorted(result.items(), key=lambda n: abs(n[1]))
n = 0
while n < 10:
    # 绝对值最小
    result_temp = result_jueduizhi[n]
    # 绝对值最大
    # result_temp = result_jueduizhi[len(result_jueduizhi)-n-1]
    temp = result_dict[result_temp[0]]
    temp_start = temp[0]
    temp_end = temp[-1]
    start, end = temp_start.split(","), temp_end.split(",")
    print("该季节起始日期：", start[0])
    print("该季节结束日期：", end[0])
    # 绝对值最小
    print("变化值：", result_jueduizhi[n][1])
    # 绝对值最大
    # print("变化值：", result_jueduizhi[len(result_jueduizhi)-n-1][1])
    print("----------------------------")
    n += 1