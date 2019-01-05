"""
【问题描述】从文件in162.txt中连续读入10个以磅为单位的重量值，将其转换为以千克为单位的值并求和，
将计算所得的和sum输出到文件out162.txt中。
            说明：一磅等于0.454千克。
【输入形式】文件输入的每一行包含10个浮点数数值，以空格分隔。
【输出形式】文件输出一个两位小数的数值sum。
【样例输入】1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
【样例输出】4.54
"""
result_sum = 0
with open("in162.txt") as datas:
    datalist = datas.read()
    result = datalist.split()
    n = 0
    while n < 10:
        result_sum += float(result[n])*0.454
        n += 1
f1 = open("out162.txt", "w")
f1.write(str("%0.2f" % result_sum) + "\n")

