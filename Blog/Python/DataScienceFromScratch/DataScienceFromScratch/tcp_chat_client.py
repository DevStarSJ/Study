#http://stackoverflow.com/questions/31639824/python-3-4-asynchio-chat-server-client-how

from socket import *
from threading import Thread

HOST = 'localhost'
PORT = 9090
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
ENCODING = 'utf-8'

s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)

def Listener():
    try:
        while True:
            data = s.recv(BUFFER_SIZE).decode(ENCODING)
            print('>', data)
    except ConnectionAbortedError:
        pass

t = Thread(target=Listener)
t.start()

try:
    while True:
        message = input('>')
        s.send(message.encode(ENCODING))
except EOFError:
    pass
finally:
    s.close()


