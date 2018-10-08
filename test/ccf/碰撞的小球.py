"""
问题描述
　　数轴上有一条长度为L（L为偶数)的线段，左端点在原点，右端点在坐标L处。有n个不计体积的小球在线段上，开始时所有的小球都
处在偶数坐标上，速度方向向右，速度大小为1单位长度每秒。
　　当小球到达线段的端点（左端点或右端点）的时候，会立即向相反的方向移动，速度大小仍然为原来大小。
　　当两个小球撞到一起的时候，两个小球会分别向与自己原来移动的方向相反的方向，以原来的速度大小继续移动。
　　现在，告诉你线段的长度L，小球数量n，以及n个小球的初始位置，请你计算t秒之后，各个小球的位置。
提示
　　因为所有小球的初始位置都为偶数，而且线段的长度为偶数，可以证明，不会有三个小球同时相撞，小球到达线段端点以及小球之间
的碰撞时刻均为整数。
　　同时也可以证明两个小球发生碰撞的位置一定是整数（但不一定是偶数）。
输入格式
　　输入的第一行包含三个整数n, L, t，用空格分隔，分别表示小球的个数、线段长度和你需要计算t秒之后小球的位置。
　　第二行包含n个整数a1, a2, …, an，用空格分隔，表示初始时刻n个小球的位置。
输出格式
　　输出一行包含n个整数，用空格分隔，第i个整数代表初始时刻位于ai的小球，在t秒之后的位置。
样例输入
3 10 5
4 6 8
样例输出
7 9 9
"""
# 接收输入的值,各个值都是str型的
n, L, t = input().split()
# 将str型转换成int型
n, L, t = int(n), int(L), int(t)
# 输入初始位置在列表里,但是这里数据全是str型的
initialPosition = input().split()
# 方向列表，1为向右，-1为向左，开始默认全是1
direction = []
# 将初始位置的值全部转换成int型，同时给方向列表对应每个位置赋值
for i in range(initialPosition.__len__()):
    # 将初始位置信息转换成int型
    initialPosition[i] = int(initialPosition[i])
    # 将方向赋值为向右，初始方向都是向右
    direction.append(1)

# 此方法用于更新方向
def updateDirection(initialPosition1, direction, L):
    # 循环判断小球的位置是否可以进行更换方向了
    for i in range(initialPosition.__len__()):
        # 如果存在某个位置的值有两个，那么就说明有两个球进行碰撞了
        if initialPosition1.count(initialPosition1[i]) == 2:
            # 那么当前这个球的方向就要取反方向了
            direction[i] = -1*direction[i]
        # 如果某一个球的位置已经在右端点了
        if initialPosition1[i] == L:
            # 那么当前这个球的方向就要取反方向了
            direction[i] = -1*direction[i]
        # 如果某一个球的位置已经在左端点了
        if initialPosition1[i] == 0:
            # 那么当前这个球的方向就要取反方向了
            direction[i] = -1*direction[i]
    # 把修改方向后的方向列表返回
    return direction

# 这t秒内的所有操作，位置信息的改变，方向信息的改变
while t > 0:
    t -= 1
    for i in range(n):
        # 移动后的位置改变
        initialPosition[i] = initialPosition[i] + direction[i]
    # 小球的方向更新
    direction = updateDirection(initialPosition, direction, L)

# 输出经过t秒后各个小球的位置
for i in initialPosition:
    print(i, end=" ")
