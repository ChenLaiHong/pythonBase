
r = open("jisuan.txt", "r")
f1 = open("jieguo.txt", "w")
# 读写操作
content = r.readlines()
for i in content:
    if i == "":
        continue
    else:
        if "+" in i:
            temp = i.split("+")
            f1.write(str("%0.2f" % (float(temp[0]) + float(temp[1]))) + '\n')
        elif "-" in i:
            temp = i.split("-")
            f1.write(str("%0.2f" % (float(temp[0]) - float(temp[1]))) + '\n')
# 关闭文件
r.close()

r1 = open("jieguo.txt", "r")
content1 = r1.readlines()
for i in content1:
    print(i, end="")
r1.close()