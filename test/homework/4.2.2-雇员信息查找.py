"""
【问题描述】
键盘输入5个雇员的信息，雇员的属性有姓、名字、电子邮箱地址、工作单位。找出姓、名字或电子邮箱地址中有"Li"或"li"出现的雇员，
输出这些雇员的信息。
【输入形式】
从键盘输入5个雇员的信息，雇员的属性有姓、名字、电子邮箱地址、工作单位。雇员信息之间隔有一行空白。
【输出形式】
输出姓、名字或电子邮箱地址中有"Li"或"li"出现的雇员的信息。雇员信息之间空一行。
【样例输入】
zhang
san
zhangsan@hotmail.com
nudt

li
si
lisi@gmail.com
nudt

wang
wu
wangwuLi@hotmail.com
nudt

zhao
zao
zhaozaoLIU@163.com
nudt

qian
qi
qianqi@163.com
nudt
【样例输出】
li
si
lisi@gmail.com
nudt

wang
wu
wangwuLi@hotmail.com
nudt
"""
temp = []
message = []
start = 0
end = temp.__len__()+1
for i in range(24):
    temp.append(input())
n = 0
while n < 5:
    for i in temp:
        if i == "":
            end = temp.index(i)
            message.append(temp[start:end])
            temp = temp[end+1:temp.__len__()+1]
            break
        else:
            continue
    n += 1
    if n == 4:
        message.append(temp)
flag = []
for i in message:
    for j in i:
        if "Li" in j or "li" in j:
            flag.append(i)
            break
for i in flag:
    for j in i:
        print(j)
    print()


