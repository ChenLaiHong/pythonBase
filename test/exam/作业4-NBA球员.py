import csv

# 计算概率的函数,最后从大到小排序返回
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

    #
    return eff_dict

csv_data = csv.reader(open('player_regular_season.csv', 'r'))

data = {}
flag = 0
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
data.pop("firstname lastname")
result = efficiency(data)
final = sorted(result.items(),key=lambda n:n[1], reverse=True)
print(final)

# for i in data:
#     print(data[i])





