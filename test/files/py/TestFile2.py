# 只读模式，打开要复制的文件
# 追加模式，打开副本文件

# source_file = open("test.txt", "r", encoding="utf-8")
# dst_file = open("result.txt", "a", encoding="utf-8")
#
# # 从源文件读取内容
# # 写入到目标文件中
# content = source_file.read()
# dst_file.write(content)
#
# # 关闭源文件和目标文件
# source_file.close()
# dst_file.close()

import os
import shutil

path = "files"
if not os.path.exists(path):
    exit()
os.chdir("files")
file_list = os.listdir("./")
print(file_list)
# 遍历所有文件
for file_name in file_list:
    # 分解文件后缀名
    #  获取最后一个.的索引位置
    index = file_name.rfind(".")
    if index == -1:
        continue
    extension = file_name[index + 1:]
    # 查看一下，是否存在同名目录
    if not os.path.exists(extension):

        # 如果不存在这样的目录，直接创建目录
        os.mkdir(extension)
    # 目录存在则移动到目录中
    shutil.move(file_name, extension)