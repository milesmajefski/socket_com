import socket


class Requester():
    def __init__(self):
        self.clientsocket = None

    def connect(self, connect_to):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect(connect_to)

    def receive(self):
        msg = self.clientsocket.recv(1024)
        print(msg.decode("utf-8"))
