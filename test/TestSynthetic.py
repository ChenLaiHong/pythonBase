# 综合训练
# 判断三位数水仙花数：百位3次方+十位3次方+个位3次方 = 数值本身
flag = True
while flag:
    number = int(input("请输入一个三位数："))
    numberOld = number
    result = number % 10
    number = number // 10
    if (result**3) + (number % 10)**3 + (number // 10)**3 == numberOld:
        print("此数为水仙花数")
        flag = False
    else:
        print("此数不是水仙花数")
