"""
【问题描述】某超市促销，对购买的第二件商品（不限商品类别）打9折。路人甲购买两件商品，请按要求输出购物小票。
【输入形式】两个商品的原价
【输出形式】两个商品的购买价格及总价（请注意保留小数点后两位有效数字）。输出的每一行占16格。价格和总价靠右对齐。
【样例输入】
5.6  78.95
【样例输出】
            5.60
           71.06
----------------
Total:     76.66
"""
price = input().split()
temp = []
i = 0
for p in price:
    temp.append('% 0.2f' % float(p))
temp[1] = str('% 0.2f' % (float(temp[1])*0.9))
for t in temp:
    print(t.rjust(16, " "))
print("-"*16)
total = float(temp[0])+float(temp[1])
print("Total:", end="")
print(('% 0.2f' % total).rjust(10, " "))



