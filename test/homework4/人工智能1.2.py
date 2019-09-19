# print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

# for x in range(1, 10):
#     for y in range(1, x+1):
#         temp = str(x)+"*"+str(y)+"="+str(x*y)
#         print(temp.ljust(10, " "),end="")
#     print("")

x = 1
while x < 10:
    y = 1
    while y <= x:
        temp = str(x)+"*"+str(y)+"="+str(x*y)
        print(temp.ljust(10, " "), end="")
        y += 1
    print("")
    x += 1
