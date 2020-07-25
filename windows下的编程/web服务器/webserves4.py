import socket
import re
from multiprocessing import Process
import sys
#
# import wgsipython # 这里导入包是一个知识点

HTML_ROOT_DIR = "./source"

PYTHON_ROOT_DIR = "./wgsipython/"


class HttpServer(object):
    """"""

    def __init__(self, port):
        super(HttpServer, self).__init__()
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 确保socket端口重用
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定默认 ip 和 端口
        self.serverSocket.bind(("", port))

        # 回调保存header属性
        self.response_header = ""

    def start_server(self):
        self.serverSocket.listen(128)
        while True:
            # 客户端连接
            client_socket, client_address = self.serverSocket.accept()
            print("[%s--%s]" % (client_address, client_address))

            # 创建进程并开启
            client_process = Process(target=self.handle_bind_client_ser, args=(client_socket,))
            client_process.start()

            # 关闭客服端一次引用
            client_socket.close()

    # 拼接响应头
    def start_response(self, status, headers):
        response_header = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            response_header += "%s:%s\r\n" % header
        self.response_header = response_header

    def handle_bind_client_ser(self, client_socket):
        # 客户端请求数据接收逐行打印
        request_data = client_socket.recv(1024)
        # 换行分割
        request_dt = request_data.splitlines()
        for line in request_dt:
            print("*" * 50)
            print(line)

        http_header_method_line = request_dt[0]
        file_name = re.match("[^/]+(/[^ ]*)", http_header_method_line.decode("utf-8")).group(1)
        print("file path is ===>%s" % file_name)

        # 判断脚本还是静态资源
        if file_name.endswith(".py"):
            # 该方法和上面直接import xxx一样的
            print("file_name-->%s" % file_name[1:-3])
            try:
                m = __import__(file_name[1:-3])
            except Exception as e:
                print(e)
                self.response_header = "HTTP/1.1 404 NOT FOUND \r\n"
                response_body = "NOT FOUND"
            else:
                # 解析报文头部的一些参数可以通过env传递
                env = {}
                response_body = m.application(env, self.start_response)
                print("返回数据\r\n%s" % response_body)
            finally:
                pass

            response = self.response_header + "\r\n" + response_body

        else:
            response_start_line = ""
            response_header = ""
            response_body = ""
            if file_name == "/":
                file_name = HTML_ROOT_DIR + "/index.html"
            else:
                file_name = HTML_ROOT_DIR + file_name

            try:
                file = open(file_name, "rb")
            except Exception as e:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_header = "Server:My Server\r\n"
                response_body = "The file is not found"
                print(e)
            else:
                file_data = file.read()
                file.close()

                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_header = "Server:My Server\r\n"
                response_body = file_data.decode("utf-8")
            finally:
                response = response_start_line + response_header + "\r\n" + response_body
                print(response)

        # 发送数据给客户端
        client_socket.send(bytes(response, "utf-8"))
        # 关闭连接
        client_socket.close()


def main():
    sys.path.insert(1, PYTHON_ROOT_DIR)
    # 包的查找模块是在path目录下面查找的，因此需要在模块下面插入指定路径
    http_server = HttpServer(8888)
    http_server.start_server()


if __name__ == "__main__":
    main()
