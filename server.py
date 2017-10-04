#!/usr/bin/python

from SocketServer import StreamRequestHandler, TCPServer
import socket


class Handler(StreamRequestHandler):
    def handle(self):
        self.wfile.write("Client %s says: %s \r\n" % (str(self.client_address), self.rfile.readline().strip()))


class Server(TCPServer):
    def __init__(self, server_address, handler_cls):
        TCPServer.__init__(self, server_address, handler_cls, bind_and_activate=False)
        self.socket = socket.fromfd(3, self.address_family, self.socket_type)


if __name__ == "__main__":
    server = Server(("0.0.0.0", 9999), Handler)
    server.serve_forever()

