# python中的列表跟java中的数组很像，但是列表里面的值不规定统一类型的
# range(start,end,step):[start,end).start:从什么开始，end：到哪里结束，step步长
num = range(1, 1000)
print(num)

nums = [1, 2, 3, 4, 5]
resultList = []
for n in nums:
    resultList.append(n**2)
print(resultList)

# 列表推导式
resultList2 = [n**2 for n in nums]
resultList3 = [n**2 for n in nums if n % 2 != 0]
print(resultList2)
print(resultList3)

