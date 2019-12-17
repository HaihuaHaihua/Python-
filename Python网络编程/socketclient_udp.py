import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ("127.0.0.1",8888)

while True:
    message = input("Input message : ")
    if message == "exit":
        break
    #向指定端口发送信息
    client.sendto(message.encode(),ip_port)
client.close()
