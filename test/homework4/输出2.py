# 把按照BMI指数排序后的数据排版输出。（不能使用列表的sort函数实现）
# 姓名       身高          体重          腰围        BMI指数       分析结果
# 张三        1.85         105.5	 108          30.82             肥胖
# 王五         1.73         76.3	  74           25.5               偏胖
# 李四         1.62         62.5         70            23.8               正常
number = int(input("请输入学生人数："))
result = []

for i in range(number):
    temp = []
    while True:
        messages = input("输入信息：").split(" ")
        try:
            if float(messages[1]) >= 2.5 or float(messages[1]) <= 0.5:
                print("身高不在合理范围")
                continue
            if float(messages[2]) >= 300 or float(messages[2]) <= 24:
                print("体重不在合理范围")
                continue
            if float(messages[3]) >= 200 or float(messages[3]) <= 50:
                print("腰围不在合理范围")
                continue

            temp.append(messages[0])
            temp.append(float(messages[1]))
            temp.append(float(messages[2]))
            temp.append(float(messages[3]))
            result.append(temp)
            break
        except Exception:
            print("输入有误！")
            continue

# 把额外计算出的信息追加进列表里面
for i in result:
    BMI = i[2] / (i[1] ** 2)

    if BMI < 18.5:
        aresult = "偏瘦"
    elif 18.5 <= BMI <= 24:
        aresult = "正常"
    elif 24 < BMI < 28:
        aresult = "偏胖"
    else:
        aresult = "肥胖"
    i.append(BMI)
    i.append(aresult)

# 根据BMI排序
result = sorted(result, key=lambda num: num[4])

# 把内容写到文件
f1 = open("resultout.txt", "w", encoding="utf-8")
f1.write('{0:{6}<10}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}'.format("姓名", "身高", "体重", "腰围", "BMI指数", "分析结果", chr(12288))+"\n")
for i in result:
    out = '{0:{6}<10}{1:<12.2f}{2:<10.1f} {3:<12.1f} {4:<11.2f} {5:<10}'.format(i[0], i[1], i[2], i[3], i[4], i[5], chr(12288))
    f1.write(out+"\n")
f1.close()