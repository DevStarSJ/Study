from socket import *
from threading import Thread
from sys import argv

HOST = 'localhost'
PORT = 9090
BUFFER_SIZE = 1024
ENCODING = 'utf-8'

if len(argv) > 1:
    PORT = int(argv[1])

ADDR = (HOST, PORT)

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDR)

def Listener():
    try:
        while True:
            data = sock.recv(BUFFER_SIZE).decode(ENCODING)
            print('>', data)
    except ConnectionAbortedError:
        pass

listener_thread = Thread(target=Listener)
listener_thread.start()

try:
    while True:
        message = input('>')
        sock.send(message.encode(ENCODING))
except EOFError:
    pass
finally:
    sock.close()
