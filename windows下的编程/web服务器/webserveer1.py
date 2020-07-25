import socket


HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))

print('Serving HTTP on port %s ...' % PORT)
while True:
    listen_socket.listen(1)
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    method = request.split(' ')[0]
    src = request.split(' ')[1]
    print(request)
    http_response = '''HTTP/1.x 200 OK\r
    Content-Type: text/html\r\n
    
    <head>
    <title> WOW</title>
    </head>
    <html>
    <body>
    <p1>Hello, World!</p1>
    </body>
    </html>
    '''
    client_connection.sendall(http_response.encode())
    client_connection.close()
