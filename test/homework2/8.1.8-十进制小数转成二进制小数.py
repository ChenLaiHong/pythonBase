"""
【问题描述】
编写程序，输入十进制小数（只考虑正数），把它转换为以字符串形式存储的二进制小数，输出该二进制小数字符串。
对于转换得到的二进制小数，小数点后最多保留10位。小数点后不足10位，则输出这些位，尾部不补0；小数点后超出10位，则直接舍弃超出部分。
【输入形式】
十进制浮点小数
【输出形式】
对应输入小数的二进制小数字符串。若整数部分或者小数部分为0，则输出0。比如输入0，则意味着输出0.0  。
【样例输入】
1.2
【样例输出】
1.0011001100
【样例说明】
输入为10进制小数，将该小数转化成二进制后输出。推荐采用字符串来处理生成的二进制数，特别要注意0的处理
"""
def changez(num):
    result = ""
    while num // 2 != 0:
        result += str(num % 2)
        num = num // 2
    result += "1"
    return result[::-1]
def change(num):
    if num == 0:
        return "0.0"
    else:
        temp = str(num).split(".")
        zhengshu = int(temp[0])
        xiaoshu = num - zhengshu

        result_zheng = changez(zhengshu)
        result_xiao = ""
        temp_xiao = str(xiaoshu).split(".")
        count_n = 0
        while int(temp_xiao[1]) != 0:
            xiaoshu = xiaoshu*2
            temp_xiao = str(xiaoshu).split(".")
            result_xiao += temp_xiao[0]
            if temp_xiao[0] == "1":
                xiaoshu -= 1
            count_n += 1
            if count_n == 10:
                break
        return result_zheng + "." + result_xiao


num = float(input())
print(change(num))