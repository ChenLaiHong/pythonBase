"""
彼得是一个喜欢电子产品的好奇男孩。有一天，这个男孩正在他的学校实验室里玩，并发现了一个装满其他学生制作的小型电子设备的盒子。
在那个盒子里面是一个只有一个显示器和两个按钮的设备。显示器显示有一个整数。按下按钮，Peter发现了每个按钮的功能 ：
    第一个按钮给显示屏上的数字加１
    第二个按钮反转数字，例如，123反转为321,150反转为51（忽略前面的零）。
最初，显示器显示数字A.在发现按钮的功能后，Peter想知道如何将A更改为B.
您在这个问题上的工作是帮助Peter找出按下按钮的最小数量，使显示数量等于B.
Input
输入由一个整数 T, 0 < T ≤ 500,其指示测试用例的数量。
在此之后，输入由T行组成，每行包含两个整数A和B，0 <  A  <  B  <10000，A等于显示器上的初始值，B等于我们需要的最终数字显示器。
Output
对于每个测试，您的程序必须输出一个等于按下最小按钮数的整数，以使显示屏上的数字A变为数字B.
Sample Input 1
4
1 9
100 301
808 909
133 233
Sample Output 1
8
4
3
3
Sample Input 2
6
1 9
100 301
808 909
133 233
123 123
0 9999
Sample Output 2
8
4
3
3
0
336
"""
# def find(nums):
#     result = 0
#     while True:
#         if nums[0] == nums[1]:
#             break
#         else:
#             if len(nums[0]) == 1 and len(nums[1]) == 1:
#                 result = int(nums[1]) - int(nums[0])
#                 break
#             else:
#                 jiafa = int(nums[0])+1
#                 jiaohuan = int(nums[0][::-1])
#                 result += 1
#                 if str(jiafa)[::-1] == nums[1] or str(jiaohuan + 1) == nums[1]:
#                     result += 1
#                     break
#                 else:
#                     nums[0] = str(jiaohuan) if int(nums[1])-jiafa > int(nums[1])-jiaohuan else str(jiafa)
#
#     print(result)
def find(nums):
    result = 0
    while True:
        if nums[0] == nums[1]:
            break
        else:
            if len(nums[0]) == 1 and len(nums[1]) == 1:
                result = int(nums[1]) - int(nums[0])
                break
            else:
                if str(int(nums[0])+1)[::-1] == nums[1] or str(int(nums[0][::-1]) + 1) == nums[1]:
                    result += 2
                    break
                else:
                    jiafa = int(nums[0])+1
                    jiaohuan = int(nums[0][::-1])
                    result += 1
                    if jiafa <= int(nums[1]) and jiaohuan <= int(nums[1]):
                        nums[0] = str(jiaohuan) if int(nums[1])-jiafa > int(nums[1])-jiaohuan else str(jiafa)
                    else:
                        nums[0] = str(jiaohuan) if jiaohuan <= int(nums[1]) else str(jiafa)

    print(result)
T = int(input())
while T > 0:
    nums = input().split()
    find(nums)
    T -= 1

