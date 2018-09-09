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
fromFile = open("xx.jpg", "rb")
fromContent = fromFile.read()
print(fromContent)
fromFile.close()

toFile = open("xx2.jpg", "wb")
content = fromContent[0: len(fromContent) // 2]
toFile.write(content)
fromFile.close()

# 增加+
# "r+"可读可写，先读再写的话不会覆盖原来的只是在后面添加


