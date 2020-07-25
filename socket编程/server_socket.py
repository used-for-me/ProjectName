import ctypes
import inspect
import socket
import threading


# tcp
class ChatSocket:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.ip_address = (ip, port)
        self.sock = socket.socket()

    def start(self):
        self.sock.bind(self.ip_address)
        self.sock.listen()
        print('绑定{}'.format(self.ip_address))
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while True:
            s, raddr = self.sock.accept()
            print(s)
            threading.Thread(target=self.recv, name='recv', args=(s,)).start()

    def recv(self, s):
        while True:
            data = s.recv(1024)
            print(data)
            self.send(s, 'ock:{}'.format(data.decode()))

    def send(self, s, data):
        s.send(data.encode())

    def stop(self):
        self.sock.close()


# def _async_raise(tid, exctype):
#   """raises the exception, performs cleanup if needed"""
#   tid = ctypes.c_long(tid)
#   if not inspect.isclass(exctype):
#     exctype = type(exctype)
#   res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
#   if res == 0:
#     raise ValueError("invalid thread id")
#   elif res != 1:
#     # """if it returns a number greater than one, you're in trouble,
#     # and you should call it again with exc=NULL to revert the effect"""
#     ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#     raise SystemError("PyThreadState_SetAsyncExc failed")
#
# def stop_thread(thread):
#   _async_raise(thread.ident, SystemExit)


chat = ChatSocket()
chat.start()

while True:
    commend = input('>>>')
    if commend.strip() == 'quit':
        chat.stop()
        break
    print(threading.enumerate())
print('quit')

# while threading.enumerate():
#     print(threading.enumerate()[-1])
#     stop_thread(threading.enumerate()[-1])
#     continue


