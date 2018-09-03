# 计算两个数的和，当输入的数存在超过一百的数时要求重新输入，当输入q时退出循环
while True:
    number1 = float(input("请输入第一个数："))
    number2 = float(input("请输入第二个数："))

    if number1 > 100 or number2 > 100:
        continue

    result = number1 + number2
    print("两数之和为：", result)
    isQ = input("是否要退出？（q：退出，其他：继续）")
    if isQ == "q":
        break