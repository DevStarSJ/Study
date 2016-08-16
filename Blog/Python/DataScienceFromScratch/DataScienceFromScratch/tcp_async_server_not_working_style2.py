import socketserver
import os

class MyRequestHandlerWithStreamRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        try:
            print("Connection from: %s" % str(self.client_address))
            #self.wfile.write(str.encode('Child %s echo>' % os.getpid()))
            #self.wfile.flush()
            request_msg = self.rfile.readline()
            self.wfile.write(str.encode("HTTP/1.0 200 Ok %s" % str(request_msg)))
            self.wfile.flush()
        except Exception as ex:
            print('e', ex)

class EchoHandler(socketserver.StreamRequestHandler):
    def handle(self):
         self.wfile.write('Child %s echo>' % os.getpid())
         self.wfile.flush()
         message = self.rfile.readline()
         self.wfile.write(message)
         print("Child %s echo'd: %r" % (os.getpid(), message))

def tcp_async_server():
    tcp_server = socketserver.ThreadingTCPServer(('localhost', 9090), RequestHandlerClass= MyRequestHandlerWithStreamRequestHandler, bind_and_activate= False)
    tcp_server.allow_reuse_address = True
    tcp_server.server_bind()
    tcp_server.server_activate()

    tcp_server.serve_forever()

if __name__ == "__main__":
    tcp_async_server()
    #server = socketserver.ThreadingTCPServer(('localhost', 9090), EchoHandler)
    #server.serve_forever()