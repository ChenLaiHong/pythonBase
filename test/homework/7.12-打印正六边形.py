"""
【问题描述】编写一个程序，输入一个正整数N，在屏幕上用*打印以N为边长的正六边形。
【输入形式】输入一个正整数N。
【输出形式】屏幕上输出以N为边长的正六边形。
【样例输入】
 4
【样例输出】
    ****
   *      *
  *        *
 *          *
  *        *
   *      *
    ****
【样例说明】输入的为一个正整数，打印输出一个以这个正整数为边长的正六边形．
###****
##*####*
#*######*
*########*
#*######*
##*####*
###****
#号代表空格。
"""
num = int(input())
temp = " "*(num-1) + "*"*num
length = temp.__len__()
result = []
number = num - 1
while number >= 0:
    result.append(temp)
    temp = ""
    for i in range(1, length+2):
        if i == number or i == length+1:
            temp += "*"
        else:
            temp += " "
    length = temp.__len__()
    number -= 1
for i in result:
    print(i)
for i in range(result.__len__()-2, -1, -1):
    print(result[i])