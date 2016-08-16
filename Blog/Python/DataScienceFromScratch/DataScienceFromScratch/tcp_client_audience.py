import socket
import sys

HOST = 'localhost'
PORT = 9099
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
ENCODING = 'utf-8'

if len(sys.argv) < 2:
    print('Please enter client ID.')
    sys.exit(0)

CLIENT_ID = sys.argv[1]

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(ADDR)
tcp_client_socket.send(CLIENT_ID.encode(ENCODING))

while True:
    received = tcp_client_socket.recv(BUFFER_SIZE)
    if not received:
        break;
    print(received)

tcp_client_socket.close()
