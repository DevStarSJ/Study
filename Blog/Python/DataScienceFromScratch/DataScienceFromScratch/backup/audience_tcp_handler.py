import socketserver
import subprocess
import sys
import time
from threading import Thread

HOST = 'localhost'
PORT = 9099
ADDR = (HOST, PORT)
ENCODING = 'utf-8'
BUFFER_SIZE = 1024

class AudienceTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address,'connected')

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    deamon_threads = True
    allow_resue_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = SimpleServer(ADDR, AudienceTcpHandler)

    cnt = 0
    try:
        while True:
            time.sleep(1)
            for client in server.get_request():
                print(client)
                #client.send(str(cnt).encode(ENCODING))
            cnt += 1
        #server.serve_forever()
    except KeyboardInterrupt: # Ctrl+C
        sys.exit(0)