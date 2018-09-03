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