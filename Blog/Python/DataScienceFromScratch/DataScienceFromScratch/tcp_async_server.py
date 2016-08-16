import socketserver
import subprocess
import sys
from threading import Thread

HOST = 'localhost'
PORT = 9090
ADDR = (HOST, PORT)
ENCODING = 'utf-8'

class SingleTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                break;

            text = data.decode(ENCODING)
            print(text)

            self.request.send('OK'.encode(ENCODING))
            #self.request.close()

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    deamon_threads = True
    allow_resue_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = SimpleServer(ADDR, SingleTcpHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt: # Ctrl+C
        sys.exit(0)