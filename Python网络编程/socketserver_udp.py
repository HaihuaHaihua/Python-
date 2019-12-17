import socket

#UDP 多客服端消息发送
#socket.AF_INET  使用ipv4协议
#socket.SOCK_DGRAM 使用udp协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ("127.0.0.1",8888)
s.bind(ip_port)

while True:
    data = s.recv(1024)
    print(data.decode())