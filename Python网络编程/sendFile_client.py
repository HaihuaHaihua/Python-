import socket

client = socket.socket()
ip_port = ("127.0.0.1",8888)
client.connect(ip_port)

#发送文件
while True:
    file = open("socketServer.py",'rb')
    for i in file:
        client.send(i)
    #发送完成
    client.send('quit'.encode())
    flag = client.recv(1024)
    if flag == b'complete':
        print("Completely Sending!")
        client.close()
    # client.close()
