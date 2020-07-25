import socket
import re
from multiprocessing import Process

HTML_ROOT_DIR = "./source"


def handle_bind_client_ser(client_socket):
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

    response_start_line = ""
    response_header = ''
    response_body = ''

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

    # 发送数据给客户端
    client_socket.send(bytes(response, "utf-8"))
    # 关闭连接
    client_socket.close()


if __name__ == "__main__":
    # 创建服务器socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 确保socket端口重用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定默认 ip 和 端口
    server_socket.bind(("", 8000))
    # 开启监听模式
    server_socket.listen(128)

    while True:
        # 客户端连接
        client_socket, client_address = server_socket.accept()
        print("[%s--%s]" % (client_address, client_address))

        # 创建进程并开启
        client_process = Process(target=handle_bind_client_ser, args=(client_socket,))
        client_process.start()

        # 关闭客服端一次引用
        client_socket.close()
