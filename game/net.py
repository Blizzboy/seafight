import socket
from json import dumps


class Network:

    def __init__(self):
        pass

    def connect(self, addr):
        pass

    def bind(self, addr):
        pass

    def send(self, message, data):
        self.sock.send(message)
        self.sock.send(dumps(data))
