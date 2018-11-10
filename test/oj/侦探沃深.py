"""
约翰·沃森（John Watson）多年来一直在为福尔摩斯（Sherlock Holmes）工作，他从未理解如何能够如此轻易地猜出谁是杀手。
然而，在某个特定的夜晚，Sherlock醉得太厉害了，他告诉约翰这个秘密是什么。
“基本亲爱的沃森”，福尔摩斯说。“它绝不是最可疑的，但却是第二个最可疑的”。在他得到这个秘密之后，约翰决定自己解决一个案件，
只是为了测试Sherlock说的是否正确。
给出一个包含N个整数的列表，表示每个人的怀疑程度，帮助John Watson决定谁是杀手
Input
将有几个测试用例。每个测试用例有一个整数开始 N (2 ≤ N ≤ 1000)，表示嫌疑人的数目。
下面会有N个不同的整数，其中第 i 个整数，代表第 i 个人的嫌疑，嫌疑值 V，1≤ V ≤10000。
当N = 0时，输入结束。
Output
根据上述方法，对于每个测试用例，打印一行，包含一个整数，代表第几个是凶手。
Sample Input 1
3
3 5 2
5
1 15 3 5 2
0
Sample Output 1
1
4
"""
def findMan(nums):
    temp = nums.copy()
    zuida = max(nums)
    first = 0
    for i in range(first, len(nums)):
        for j in range(i, len(nums)):
            if nums[j] == zuida:
                first = j
                nums.remove(nums[j])
                break
    second = max(nums)
    weizhi = temp.index(second)
    return weizhi+1

result = []
while True:
    N = int(input())
    if N == 0:
        break
    else:
        nums = input().split()
        nums = [int(n) for n in nums]
        result.append(findMan(nums))
for i in result:
    print(i)
