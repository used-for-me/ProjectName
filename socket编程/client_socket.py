import socket
import threading


# tcp
class ChatSocket:
    def __init__(self, ip='127.0.0.1', port=8887, raddr=('127.0.0.1', 9999)):
        self.ip_address = (ip, port)
        self.sock = socket.socket()
        self.raddr = raddr

    def start(self):
        self.sock.bind(self.ip_address)
        # self.sock.listen()
        print('绑定{}'.format(self.ip_address))
        threading.Thread(target=self.connect, name='connect').start()

    def connect(self):
        self.sock.connect(self.raddr)
        threading.Thread(target=self.recv, name='recv', args=(self.sock,)).start()

    def recv(self, s):
        while True:
            data = s.recv(1024)
            print(data)

    def send(self):
        data = input('data：')
        self.sock.send(data.encode())

    def stop(self):
        self.sock.close()


chat = ChatSocket()
chat.start()

while True:
    commend = input('>>>')
    if commend.strip() == 'quit':
        chat.stop()
        break
    elif commend.strip() == 'send':
        chat.send()
    print(threading.enumerate())
