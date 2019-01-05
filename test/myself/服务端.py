# 1搭建网络连接
from socket import *
import os
import sys


def do_login(s, user, name, addr):
    if (name in user) or name == '管理员':
        s.sendto('该用户存在'.encode, addr)
        return
    s.sendto(b'OK', addr)
    # 通知所有人
    msg = '\n欢迎 %s 进入聊天室' % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 将用户插入字典
    user[name] = addr

    # print('登录')


def do_chat(s, user, name, text):
    msg = '\n%-4s 说:%s' % (name, text)
    # 发给所有人,除了自己
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
            # print('聊天')


def do_quit(s, user, name):
    del user[name]
    msg = '\n' + name + '离开了聊天室'
    for i in user:
        s.sendto(msg.encode(), user[i])
        # print('退出')


# 接收客户端请求并处理
def do_child(s):
    # 用于存储用户{'z':(172.60.50.51,8956)}
    # 可变类型,修改可被影响
    user = {}
    # 循环接收个个客户端请求并处理
    while True:
        msg, addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        # 判断请求类型进行处理
        if msgList[0] == 'L':
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == 'C':
            do_chat(s, user, msgList[1], ' '.join(msgList[2:]))
        elif msgList[0] == 'Q':
            do_quit(s, user, msgList[1])


# 发送管理员消息
def do_parent(s, addr):
    while True:
        msg = input('管理员消息:')
        msg = 'C 管理员 ' + msg
        s.sendto(msg.encode(), addr)


# 1创建套接字,创建连接,创建父子进程
def main():
    # server address
    ADDR = ('0.0.0.0', 10010)
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    # 创建父子进程,并且防止僵尸进程
    pid = os.fork()

    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        # 创建二级子进程
        pid0 = os.fork()
        if pid0 < 0:
            sys.exit('创建失败')
        elif pid0 == 0:
            # 执行子进程功能
            do_child(s)
        else:
            os._exit(0)
    else:
        os.wait()
        # 执行父进程功能
        do_parent(s, ADDR)


if __name__ == '__main__':
    main()
