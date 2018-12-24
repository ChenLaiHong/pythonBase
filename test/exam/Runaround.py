"""
编写一个程序，输入一个2~7位的整数，然后判断它是否是一个runaround数。若是则输出Yes, 否则输出No。一个N位的runaround数具有以下的特点。
（1）       该整数有N位，每一位数字在1~9之间。
（2）       这些数字构成了一个序列，序列中每位数字的值指明了下一个序列数所在的位置。
例如，假设当前数字为2，则往右走2步，即到达下一个序列数。若在此过程中到达了该整数的右边界，则返回到它的最左边。
（3）       序列起始于该整数最左边的数字，并且在遍历该整数的所有数字各一次后，又回到了起始位置。
（4）       该整数的各位数字各不相同，没有重复。
例如，对于整数81362，可以通过以下步骤来验证它是否是一个runaround数。
（1）       从最左边的数字（即8）开始：8 1 3 6 2。
（2）       往右走8步，停在6上面（注意走到右边界时要返回到最左边）：8 1 3 6 2
（3）       往右走6步，停在2上面：8 1 3 62
（4）       往右走2步，停在1上面：81 3 62
（5）       往右走1步，停在3上面：81362
（6）       往右走3步，即回到了起始位置：81362
输入:
81362
输出:
Yes
"""
num = input()
flag = 0
for i in range(len(num)):
    for j in range(flag,len(num)):
        pass