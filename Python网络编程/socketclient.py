import socket

client = socket.socket()

#绑定服务器的ip地址和端口号
ip_port = ("127.0.0.1",8888)
#客户端请求
client.connect(ip_port)

# data = client.recv(1024)
# print(data.decode()) #对byte类型数据进行解码

#向服务端发信息
while True:
    #接收消息
    data = client.recv(1024)
    print(data.decode())
    #发送消息
    msg = input("input message : ")
    client.send(msg.encode())
    if msg == "exit":
        break
    #消息处理
    data = client.recv(1024)
    print(data.decode())
    