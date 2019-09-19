# 条件判断语句，循环语句的使用，列表的使用。
# 要求：首先输入学生人数，并根据输入的人数输入姓名（n个）、身高（0.5<height<2.5），
# 体重(20<weight<300)，腰围(50<waistline<200)，输入的值如果不在合理范围要输出提醒信息并要求重新输入。
# 计算出每位同学的BMI指数，并按照BMI指数排序，判断出每个同学属于偏瘦（<18.5）、正常（>=18.5 and <24）
# 偏胖(>24 and <28）、肥胖（>28）的哪一种情况。
# 把按照BMI指数排序后的数据排版输出。（不能使用列表的sort函数实现）
# 姓名       身高          体重          腰围        BMI指数       分析结果
# 张三        1.85         105.5	 108          30.82             肥胖
# 王五         1.73         76.3	  74           25.5               偏胖
# 李四         1.62         62.5         70            23.8               正常

number = int(input("请输入学生人数："))
result = []

for i in range(number):
    temp = []
    name = input("输入姓名：")

    while True:
        height = float(input("输入身高："))
        if height >= 2.5 or height <= 0.5:
            print("身高不在合理范围")
        else:
            break
    while True:
        weight = float(input("输入体重："))
        if weight >= 300 or weight <= 24:
            print("体重不在合理范围")
        else:
            break
    while True:
        yaowei = float(input("输入腰围："))
        if yaowei >= 200 or yaowei <= 50:
            print("腰围不在合理范围")
        else:
            break
    temp.append(name)
    temp.append(height)
    temp.append(weight)
    temp.append(yaowei)
    result.append(temp)
print('{0:{6}<10}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}'.format("姓名", "身高", "体重", "腰围", "BMI指数", "分析结果", chr(12288)))
for i in result:
    BMI = i[2] / (i[1] ** 2)

    if BMI < 18.5:
        result = "偏瘦"
    elif 18.5 <= BMI <= 24:
        result = "正常"
    elif 24 < BMI < 28:
        result = "偏胖"
    else:
        result = "肥胖"

    print('{0:{6}<10}{1:<12.2f}{2:<10.1f} {3:<12.1f} {4:<11.2f} {5:<10}'.format(i[0], i[1], i[2], i[3], BMI, result, chr(12288)))
