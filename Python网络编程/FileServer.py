import socket

ser = socket.socket()
ip_port = ("127.0.0.1",8888)
ser.bind(ip_port)
ser.listen(5)

while True:
    conn , address = ser.accept()
    while True:
        file = open("newfile",'ab')
        data = conn.recv(1024)
        if data == b'quit':
            conn.send('complete'.encode())
            break
        file.write(data)
    print("Completely!")

