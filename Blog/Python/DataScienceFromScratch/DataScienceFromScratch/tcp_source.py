import socket

HOST = 'localhost'
PORT = 9090
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break;
    tcp_client_socket.send(str.encode(data))
    received = tcp_client_socket.recv(BUFFER_SIZE)
    if not received:
        break;
    print(received)

tcp_client_socket.close()