import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.4.36.40', 5550))
sock.listen(5)
print('服务器', socket.gethostbyname('10.4.36.40'), '监听 ...')
mydict = dict()
mylist = list()

#把whatToSay传给除了exceptNum的所有人
def tellOthers(exceptNum, whatToSay):
    for c in mylist:
        if c.fileno() != exceptNum :
            try:
                c.send(whatToSay.encode())
            except:
                pass
def subThreadIn(myconnection, connNumber):
    nickname = myconnection.recv(1024).decode()
    mydict[myconnection.fileno()] = nickname
    mylist.append(myconnection)
    print('连接', connNumber, ' 昵称为 :', nickname)
    tellOthers(connNumber, '【系统提示：'+mydict[connNumber]+' 进入聊天室】')
    while True:
        try:
            recvedMsg = myconnection.recv(1024).decode()
            if recvedMsg:
                print(mydict[connNumber], ':', recvedMsg)
                tellOthers(connNumber, mydict[connNumber]+' :'+recvedMsg)
        except (OSError, ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(mydict[connNumber], '退出,还剩 ', len(mylist), ' 个人')
            tellOthers(connNumber, '【系统提示：'+mydict[connNumber]+' 离开聊天室】')
            myconnection.close()
            return
while True:
    connection, addr = sock.accept()
    print('收到新的连接', connection.getsockname(), connection.fileno())
    try:
        buf = connection.recv(1024).decode()
        if buf == '1':
            connection.send(b'welcome to server!')
            #为当前连接开辟一个新的线程
            mythread = threading.Thread(target=subThreadIn, args=(connection, connection.fileno()))
            mythread.setDaemon(True)
            mythread.start()
        else:
            connection.send(b'please go out!')
            connection.close()
    except :
        pass
 
 
 