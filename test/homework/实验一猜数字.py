import random
import math
continuing = True
temp = 0
while continuing:
    n = random.randint(50, 100000)
    number = random.randint(1, n)
    print("我已经想好了50到100000之间的一个数。")
    cishu = int(math.log(n, 2))
    for i in range(cishu):
        print("你猜一猜看是什么数：")
        guess = int(input())
        if guess == number:
            print("你猜对了。恭喜！")
            temp = 1
            break
        elif guess < number:
            print("猜小了")
        else:
            print("猜大了")
    if temp == 0:
        print("你猜的都不对。我想的数字是" + str(number) + ".")

    print("再猜一轮？(yes/no)")
    continuing = input().lower().startswith('y')
