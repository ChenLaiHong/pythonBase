# -*-coding:utf-8-*-

# socket 服务端和客户端    服务端监听   客户端的请求  链接确认

import socket
import threading

outString = ''
inString = ''
# nick = ''


# 发送信息的函数
def DealOut(sock):
    global nick, outString  # 声明为全局变量，进行赋值,这样才可以生效
    while True:
        outString = input()  # 输入
        outString = nick + ':' + outString  # 拼接cd
        sock.send(outString.encode("utf-8"))  # 发送


# 接收信息
def DealIn(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024)
            if not inString:
                break
            if outString != inString:
                print(inString.decode())
        except:
            break


nick = input('请输入昵称:')  # 名字
ip = input('输入ip地址:')  # ip地址

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字,默认为ipv4
sock.connect((ip, 3333))  # 发起请求，接收的是一个元组
# print(nick,type(nick))
sock.send(nick.encode("utf-8"))

# 多线程  接收信息 发送信息
thin = threading.Thread(target=DealIn, args=(sock,))  # 调用threading 创建一个接收信息的线程'
thin.start()

thout = threading.Thread(target=DealOut, args=(sock,))  # 创建一个发送信息的线程，声明是一个元组
thout.start()
