"""
9. 	

【问题描述】
已知1980年1月1日是星期二。
任意输入一个日期，求这一天是星期几。
【输入形式】
从键盘输入一行字符串"Y-M-D"，是一个有效的公历日期。其中Y为年（1980<=Y<=3000），M为月，D为天，都不带有前缀0。
【输出形式】
在屏幕输出结果。
输出只有一行，是代表该日星期的字符串。对于星期一至星期日，分别输出Monday、Tuesday、Wednesday、Thursday、Friday、Saturday、Sunday。
在行末要输出一个回车符。判断闰年的算法是：
年份能被4整除并且不能被100整除，或者能被四百整除。
【输入样例】
2004-1-6
【输出样例】
Tuesday
"""
import datetime
xingqi = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time = input().split("-")
year, month, day = int(time[0]),int(time[1]),int(time[2])
#某个日期星期几
anyday=datetime.datetime(year,month,day).strftime("%w")
print(xingqi[int(anyday)-1])
