# 文件操作
# 打开文件
# "r"只读；
# "w"只写，文件不存在会自动创建；指针在文件头
# "a"追加，文件不存在会自动创建，指针在文件末尾
# f = open("test.txt", "a", encoding="utf-8")
#
# # 读写操作
# # content = f.read()
# # print(content)
#
# f.write("张三、李四")
#
# # 关闭文件
# f.close()

# 操作图片,增加b是操作二进制
# fromFile = open("xx.jpg", "rb")
# fromContent = fromFile.read()
# print(fromContent)
# fromFile.close()
#
# toFile = open("xx2.jpg", "wb")
# content = fromContent[0: len(fromContent) // 2]
# toFile.write(content)
# fromFile.close()

# 增加+
# "r+"可读可写，先读再写的话不会覆盖原来的只是在后面添加


# 定位
# f.seek(偏移量，[0,1,2]),0:开头；1:当前位置；2：文件末尾（偏移量只能是负的）
# 注意：文本文件的操作模式下（不带b）只能写0
#       如果想写1/2，必须在二进制文件操作模式下（带b）
# f = open("test.txt", "r", encoding="utf-8")
# # 打印当前指针的位置,文件指针默认在文件最开始的地方
# print(f.tell())
# # 将指针移动三位（seek方法用来移动指针的位置）
# f.seek(3)
# # 再次打印指针的位置
# print(f.tell())
# # 读取当前指针位置到文件最后的内容
# print(f.read())
# f.close()



# f = open("xx.jpg", "rb")
# # 打印当前指针的位置,文件指针默认在文件最开始的地方
# print(f.tell())
# # 将指针移动三位（seek方法用来移动指针的位置）
# f.seek(-3, 2)
# # 再次打印指针的位置
# print(f.tell())
# # 读取当前指针位置到文件最后的内容
# print(f.read())
# f.close()



# f.read(len):len:读取文件内容的长度，默认是文件所有内容


# f = open("test.txt", "r", encoding="utf-8")
# print(f.read(3))
# # 将指针移动两位再读
# f.seek(2)
# print(f.read(3))
# # print(l)
#
# f.close()


# f.readLine([limit]):读取一行数据

# print(f.readline(), end="")

# f.readLines()会自动的将文件按换行符进行处理
# 将处理的每一行组成一个列表返回
# print(f.readlines())

# for i in f:
#     print(i, end="")


import os
os.rename("x.jpg", "xx.jpg")

