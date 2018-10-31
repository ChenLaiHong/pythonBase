import random
# 综合训练
# 判断三位数水仙花数：百位3次方+十位3次方+个位3次方 = 数值本身
flag = True
while flag:
    number = int(input("请输入一个三位数："))
    numberOld = number
    result = number % 10
    number = number // 10
    if (result ** 3) + (number % 10) ** 3 + (number // 10) ** 3 == numberOld:
        print("此数为水仙花数")
        flag = False
    else:
        print("此数不是水仙花数")

# 猜数字
number2 = random.randint(1, 100)
num = 0
while True:
    result = int(input("请输入你猜的数字："))
    num += 1
    if result > number2:
        print("你猜的数字大了，请重新猜！")
    elif result < number2:
        print("你猜的数字小了，请重新猜！")
    else:
        print("你猜的对了,数字就是%d,一共猜了%d 次" % (number2, num))
        break
