import csv

# 处理csv文件
def handle(csv_data):
    data = {}
    # 将需要用到的数据封装到字典里面，名称是key,值为二维列表
    for i in csv_data:
        if len(i) < 23:
            continue
        name = i[2] + " " + i[3]
        temp_data = [i[6],i[7],i[8],i[11],i[12],i[13],i[14],i[15],i[17],i[18],i[19],i[20]]
        if name in data:
            data[name].append(temp_data)
        else:
            data[name] = [temp_data]
    # 去掉第一行
    data.pop("firstname lastname")
    return data

# 计算各个球员的上场时间
def minutes(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                if i in eff_dict:
                    eff_dict[i] += int(j[1])
                else:
                    eff_dict[i] = int(j[1])
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)

# 计算各个球员的效率
def efficiency(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                nums = [int(n) for n in j]
                temp_result = ((nums[2]+nums[3]+nums[4]+nums[5]+nums[6])-((nums[8]-nums[9])+(nums[10]-nums[11])+nums[7]))//nums[0]
                if i in eff_dict:
                    eff_dict[i] += temp_result
                else:
                    eff_dict[i] = temp_result
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)

# 计算每个球员整个生涯的比赛场数
def gp(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                if i in eff_dict:
                    eff_dict[i] += int(j[0])
                else:
                    eff_dict[i] = int(j[0])
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)

# 计算各个球员得分
def pts(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                if i in eff_dict:
                    eff_dict[i] += int(j[2])
                else:
                    eff_dict[i] = int(j[2])
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)

# 计算各个球员篮板
def reb(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                if i in eff_dict:
                    eff_dict[i] += int(j[3])
                else:
                    eff_dict[i] = int(j[3])
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)

# 计算各个球员罚球
def fta(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                if i in eff_dict:
                    eff_dict[i] += int(j[10])
                else:
                    eff_dict[i] = int(j[10])
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)

# 计算各个球员罚球命中
def turnover(data):
    eff_dict = {}
    for i in data:
        for j in data[i]:
            if 'NULL' not in j and 'N' not in j:
                if i in eff_dict:
                    eff_dict[i] += int(j[7])
                else:
                    eff_dict[i] = int(j[7])
    return sorted(eff_dict.items(),key=lambda n:n[1], reverse=True)
# 读取csv文件的内容
csv_data = csv.reader(open('player_regular_season.csv', 'r'))
# 调用处理文件的函数
data = handle(csv_data)
# 调用计算效率的函数
# result = efficiency(data)
# 输入
# num = int(input())
# # 计算效率：第一二行的静态数据
# times = 27-len("Name")-len("efficiency")/2
# space = " "*int(times)
# print(5*" ", "Name", space, "efficiency")
# print(45*"-")
# for i in result:
#     if num == 0:
#         break
#     times_temp = 20-len(i[0])
#     space = " " * times_temp
#     print(i[0], space, ":", "%12d" % i[1])
#     num -= 1

# 调用计算比赛各种计算的函数，把函数名对应更改就行
result = turnover(data)
# 输入
num = int(input())
# 第一二行的静态数据
times = 27-len("turnover")/2 - len("Name")
space = " "*int(times)
print("turnover", space, "Name")
print(45*"-")
for i in result:
    if num == 0:
        break
    times_temp = 20-len(str(i[1]))
    space = " " * times_temp
    print(i[1], space, ":", "%12s" % i[0])
    num -= 1




