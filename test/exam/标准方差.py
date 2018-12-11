"""
【问题描述】
编写一个函数std，计算一个实数数组的所有元素的标准方差。并编写程序输入实数数组，调用函数求出标准方差而后输出。
注：需要在程序开头导入math模块，写法是：import math。求平方根使用函数sqrt()，例如x = 3.5，则x的平方根为mtah.sqrt(x)。
       标准方差计算公式如下，其中x(i)指的是数组中下标为i的元素；x上面带一横的指的是所有元素的平均值。
       【输入格式】
输入有两行。
第一行表示实数数组的元素个数N（N < 1000）;
第二行表示输入的实数数组，包含N个元素，元素之间用空格分隔。
【输出格式】
输出只有一行，即输入数组的标准方差；保留3位小数。
【样例输入】
4
23.45 35.7 54.89 47
【样例输出】
11.225
"""
#每一个数与这个数列的平均值的差的平方和，除以这个数列的项数，再开根号
import math
def avg(nums):
    he = 0
    for i in nums:
        he += float(i)
    return he / len(nums)

def std(nums, pingjun):
    temp = 0
    for i in nums:
        temp += (float(i) - pingjun) ** 2
    return math.sqrt(temp/len(nums))

num = int(input())
nums = input().split()
pingjun = avg(nums)
print("%0.3f" % (std(nums, pingjun)))

