# 例10-1-1  读取整个文件

with open('10-1-data.txt') as datafile:
    lines = datafile.read()
    print(type(lines))
    print(lines)
    print("lines[-1]:", lines[-1])

    # with语句写法：
    #   with ... as ...:
    #       with语句块

    # newlines = datafile.read()  #本行会报错，ValueError: I/O operation on closed file.
    # 错误信息是说文件已经关闭，不能再进行I/O操作（输入/输出操作）。
