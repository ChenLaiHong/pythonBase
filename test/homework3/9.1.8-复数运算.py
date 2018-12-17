"""
【问题描述】
编程实现两个复数的运算。
要求：
（1）定义一个类来实现复数。
（2）复数之间的加法、减法、乘法和除法分别用方法来实现。
【输入形式】
运算符号(+,-,*,/) a b c d. 
如果是除法，c，d不同时为0
【输出形式】
a+bi，当b>0时。a-bi，当b<0时。a,b都保留两位小数。
【样例输入】
-  2.5 3.6 1.5 4.9
【样例输出】
1.00-1.30i
【样例输入】
+  1.234 -3.456 -1.234 3.456
【样例输出】
0.00+0.00
"""
class Complex:
    def __init__(self, num1_shi, num1_xu,num2_shi,num2_xu):

        self.num1_shi = num1_shi
        self.num1_xu = num1_xu
        self.num2_shi = num2_shi
        self.num2_xu = num2_xu
        self.jiafa = ""
        self.jianfa = ""
        self.chengfa = ""
        self.chufa = ""
    def jia(self):
        if float(self.num1_xu)+float(self.num2_xu) < 0:
            temp = str('%0.2f' % (float(self.num1_shi)+float(self.num2_shi)))+str('%0.2f' % (float(self.num1_xu)+float(self.num2_xu)))+"i"
        else:
            temp = str('%0.2f' % (float(self.num1_shi)+float(self.num2_shi)))+"+"+str('%0.2f' %(float(self.num1_xu)+float(self.num2_xu)))+"i"
        self.jiafa = temp
    def jian(self):
        if float(self.num1_xu)-float(self.num2_xu) < 0:
            temp = str('%0.2f' % (float(self.num1_shi)-float(self.num2_shi)))+str('%0.2f' % (float(self.num1_xu)-float(self.num2_xu)))+"i"
        else:
            temp = str('%0.2f' % (float(self.num1_shi)-float(self.num2_shi)))+"+"+str('%0.2f' % (float(self.num1_xu)-float(self.num2_xu)))+"i"
        self.jianfa = temp
    def cheng(self):
        if float(self.num1_xu)*float(self.num2_shi) + float(self.num1_shi)*float(self.num2_xu) < 0:
            temp = str('%0.2f' % (float(self.num1_shi)*float(self.num2_shi)-float(self.num1_xu)*float(self.num2_xu)))+str('%0.2f' % (float(self.num2_shi)*float(self.num1_xu)+float(self.num1_shi)*float(self.num2_xu)))+"i"
        else:
            temp = str('%0.2f' % (float(self.num1_shi)*float(self.num2_shi)-float(self.num1_xu)*float(self.num2_xu)))+"+"+str('%0.2f' % (float(self.num2_shi)*float(self.num1_xu)+float(self.num1_shi)*float(self.num2_xu)))+"i"
        self.chengfa = temp
    def chu(self):
        temp1 = float(self.num2_shi) ** 2 + float(self.num2_xu) ** 2
        temp2 = float(self.num1_shi) * float(self.num2_shi) + float(self.num1_xu) * float(self.num2_xu)
        temp3 = float(self.num1_xu) * float(self.num2_shi) - float(self.num1_shi) * float(self.num2_xu)
        if temp3/temp1 < 0:
            temp = str('%0.2f' % (temp2/temp1))+str('%0.2f' % (temp3/temp1))+"i"
        else:
            temp = str('%0.2f' % (temp2/temp1))+"+"+str('%0.2f' % (temp3/temp1))+"i"
        self.chufa = temp

nums = input().split()
fuhao = nums[0]
jisuan = Complex(nums[1],nums[2],nums[3],nums[4])
if fuhao == "+":
    jisuan.jia()
    print(jisuan.jiafa)
elif fuhao == "-":
    jisuan.jian()
    print(jisuan.jianfa)
elif fuhao == "*":
    jisuan.cheng()
    print(jisuan.chengfa)
elif fuhao == "/":
    jisuan.chu()
    print(jisuan.chufa)
