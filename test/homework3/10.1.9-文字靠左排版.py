"""
【输入形式】
待排版的参演人员名单从当前目录下的listin.txt文件中读入；表示冒号':'位置的整数从标准输入读入。
【输出形式】
排版后的参演人员名单输出到当前目录下的listout.txt中。
【输入样例】
假设文件listin.txt内容为：
   Digital Intermediate by :   EFILM 
Supervising    Digital Colorist : STEVEN J. SCOTT  
 Second Colorist :ANDREW FRANCIS
 Digital Intermediate Producer:LOAN PHAN
Digital  Intermediate Editor:  DEVON MILLER     
表示冒号固定位置的整数为：40
【输出样例】
文件listout.txt中的内容应为：
Digital Intermediate by             :   EFILM 
Supervising    Digital Colorist    : STEVEN J. SCOTT  
Second Colorist                    :ANDREW FRANCIS
Digital Intermediate Producer      :LOAN PHAN
Digital  Intermediate Editor       :  DEVON MILLER  
"""
r = open("listin.txt", "r")
f1 = open("listout.txt", "w")
# 读写操作
content = r.readlines()
result = []
for i in content:
    result.append(i.split())
# 关闭文件
r.close()
temp = ""
for i in result:
    for j in i:
        if j != ":":
            temp += j + " "
        else:
            temp = temp.ljust(39)
            temp += ": "
    f1.write(temp[0:len(temp)-1]+"\n")
    temp = ""
f1.close()