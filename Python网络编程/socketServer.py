import socket
import random

s = socket.socket()
ip_port = ("127.0.0.1",8888)
#绑定监听
s.bind(ip_port)
#设置最多连接数
s.listen(5)
while True:
    print("Waiting...")

    #服务端接受数据和客户端地址
    conn,address = s.accept()

    #python3中网络数据为byte类型 其他类型需要进行编码
    message = "hello client"
    conn.send(message.encode())

    #服务器接收客户端消息
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
        #处理接收的客户端数据
        conn.send(data)
        conn.send(str(random.randint(1,1000)).encode())
    #完成消息发送后关闭
    #s.close()  