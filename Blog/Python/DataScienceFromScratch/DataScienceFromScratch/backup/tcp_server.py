import socket

HOST = ''
PORT_EVENT_SOURCE = 9090
PORT_CLIENT_USER = 9099
ADDR = (HOST, PORT_EVENT_SOURCE)
BUFFER_SIZE = 1024

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(ADDR)
tcp_server_socket.listen(10)

while True:
    print('Waiting for connection..')
    tcp_client_socket, addr = tcp_server_socket.accept()
    print('...connected from:', addr)

    while True:
        data = tcp_client_socket.recv(BUFFER_SIZE)
        if not data:
            break;
        tcp_client_socket.send(data)

    tcp_client_socket.close()
