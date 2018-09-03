# 九九乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print(i, "*", j, "=", i*j, end="\t")
    print()


print("===================================================")
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d" % (j, i, j*i), end="\t")
    print()


# 补充pass语句，pass语句是个空语句，只是为了确保语句的完整性，就是当还不写循环体语句或者其他语句的时候可以写
# 例如：
age = 19
if age > 18:
    pass
else:
    pass

for a in range(1,10):
    pass