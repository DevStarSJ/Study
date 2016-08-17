#http://stackoverflow.com/questions/31639824/python-3-4-asynchio-chat-server-client-how

from socket import *
from threading import Thread

HOST = 'localhost'
PORT = 9090
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
ENCODING = 'utf-8'

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
