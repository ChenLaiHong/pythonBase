"""
【问题描述】
定义复数类Complex，使用方法实现复数的加法、减法、乘法，所有方法都返回Complex类型的对象。
程序输入两个复数，而后依次输出加法结果，减法结果和乘法结果。
【输入形式】
每个复数的输入形式是：(实部，虚部）。实部和虚部都是整数。
【输出形式】
以"(被加数)+(加数)=结果"形式输出每一个结果。中间不带任何空格。注意被加数和加数两边的括号。
每个复数都以"实部+虚部i"形式输出。即使实部或虚部为零，也不要省略。
【样例输入】
(1,0)  
(0,1)
【样例输出】
(1+0i)+(0+1i)=1+1i
(1+0i)-(0+1i)=1-1i
(1+0i)*(0+1i)=0+1i
"""
class Complex:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.num1_shi = self.num1[0]
        self.num1_xu = self.num1[1]
        self.num2_shi = self.num2[0]
        self.num2_xu = self.num2[1]
        self.jiafa = ""
        self.jianfa = ""
        self.chengfa = ""
    def jia(self):
        if int(self.num1_xu)+int(self.num2_xu) < 0:
            temp = "("+self.num1_shi+"+"+self.num1_xu+"i)+("+self.num2_shi+"+"+self.num2_xu+"i)="+str(int(self.num1_shi)+int(self.num2_shi))+str(int(self.num1_xu)+int(self.num2_xu))+"i"
        else:
            temp = "("+self.num1_shi+"+"+self.num1_xu+"i)+("+self.num2_shi+"+"+self.num2_xu+"i)="+str(int(self.num1_shi)+int(self.num2_shi))+"+"+str(int(self.num1_xu)+int(self.num2_xu))+"i"
        self.jiafa = temp
    def jian(self):
        if int(self.num1_xu)-int(self.num2_xu) < 0:
            temp = "("+self.num1_shi+"+"+self.num1_xu+"i)-("+self.num2_shi+"+"+self.num2_xu+"i)="+str(int(self.num1_shi)-int(self.num2_shi))+str(int(self.num1_xu)-int(self.num2_xu))+"i"
        else:
            temp = "("+self.num1_shi+"+"+self.num1_xu+"i)-("+self.num2_shi+"+"+self.num2_xu+"i)="+str(int(self.num1_shi)-int(self.num2_shi))+"+"+str(int(self.num1_xu)-int(self.num2_xu))+"i"
        self.jianfa = temp
    def cheng(self):
        if int(self.num1_xu)*int(self.num2_xu) < 0:
            temp = "("+self.num1_shi+"+"+self.num1_xu+"i)*("+self.num2_shi+"+"+self.num2_xu+"i)="+str(int(self.num1_shi)*int(self.num2_shi)-int(self.num1_xu)*int(self.num2_xu))+str(int(self.num2_shi)*int(self.num1_xu)+int(self.num1_shi)*int(self.num2_xu))+"i"
        else:
            temp = "("+self.num1_shi+"+"+self.num1_xu+"i)*("+self.num2_shi+"+"+self.num2_xu+"i)="+str(int(self.num1_shi)*int(self.num2_shi)-int(self.num1_xu)*int(self.num2_xu))+"+"+str(int(self.num2_shi)*int(self.num1_xu)+int(self.num1_shi)*int(self.num2_xu))+"i"

        self.chengfa = temp
# (5+0i)+(-3+0i)
num1 = input()
num2 = input()
num1 = num1[1:len(num1)-1].split(",")
num2 = num2[1:len(num2)-1].split(",")
jisuan = Complex(num1,num2)
jisuan.jia()
print(jisuan.jiafa)
jisuan.jian()
print(jisuan.jianfa)
jisuan.cheng()
print(jisuan.chengfa)