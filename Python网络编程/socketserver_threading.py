#使用socketserver中多线程实现非阻塞
import socketserver
import random

class Server(socketserver.BaseRequestHandler):
    def setup(self):
        pass
    def handle(self):
        conn = self.request
        message = "Hello client"
        conn.send(message.encode())
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == b'exit':
                break
            conn.send(data)
            conn.send(str(random.randint(1,1000)).encode())
        conn.close()
    def finish(self):
        pass

if __name__ == "__main__":
    ser = socketserver.ThreadingTCPServer(("127.0.0.1",8888),Server)
    ser.serve_forever()