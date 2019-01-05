import socket
import threading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.4.36.40', 5550))
sock.send(b'1')
print(sock.recv(1024).decode())
nickName = input('请输入昵称: ')
sock.send(nickName.encode())
def sendThreadFunc():
    while True:
        try:
            myword = input()
            sock.send(myword.encode())
        except ConnectionAbortedError:
            print('服务器关闭了连接!')
        except ConnectionResetError:
            print('服务器未启动!')
def recvThreadFunc():
    while True:
        try:
            otherword = sock.recv(1024)
            if otherword:
                print(otherword.decode())
            else:
                pass
        except ConnectionAbortedError:
            print('服务器关闭了连接!')
        except ConnectionResetError:
            print('服务器未启动!')
th1 = threading.Thread(target=sendThreadFunc)
th2 = threading.Thread(target=recvThreadFunc)
threads = [th1, th2]

for t in threads :
    t.setDaemon(True)
    t.start()
t.join()