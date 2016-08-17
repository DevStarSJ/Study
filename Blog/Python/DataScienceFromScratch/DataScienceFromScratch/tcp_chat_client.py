import socket
import subprocess
import sys
import multiprocessing
import uuid
from threading import Thread

HOST = 'localhost'
PORT = 9090
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
ENCODING = 'utf-8'

list_process = []

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(ADDR)

def send_work():
    while True:
        data = input('> ')
        if not data:
            break;
        tcp_client_socket.send(data.encode(ENCODING))
    

def receive_work():
    while True:
        received = tcp_client_socket.recv(BUFFER_SIZE)
        if not received:
            break;
        print(received)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=send_work)
    #process2 = multiprocessing.Process(target=receive_work)

    list_process.append(process1)
    #list_process.append(process2)

    for p in list_process:
        p.start()

    for p in list_process:
        p.join()

    tcp_client_socket.close()
