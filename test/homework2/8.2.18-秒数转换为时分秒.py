"""
【问题描述】写一个函数conv()，该函数将以秒为单位输入的一个时间值，转化成
      时、分、秒（即转换为"几小时几分几秒"的形式），以一个元组的形式返回。元组的第一个元素是小时数，第二个元素是分钟数，
      第三个元素是秒数。
【输入形式】秒数
【输出形式】几小时几分几秒

【样例输入】3661
【样例输出】1h1m1s
"""
def conv(seconds):
    result = []
    result.append(seconds // 3600)
    result.append((seconds % 3600)//60)
    result.append((seconds % 3600)%60)
    return result



seconds = int(input())
hms = conv(seconds)
print(str(hms[0]) + 'h' + str(hms[1]) + 'm' + str(hms[2]) + 's')