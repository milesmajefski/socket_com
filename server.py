import socket
import time
import asyncio


class Replier:
    def __init__(self):
        self.serversocket = None

    def connect(self, connect_to):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(connect_to)
        self.serversocket.listen(5)

    async def accept_request(self):
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = self.s.accept()
        # await self.s.accept()
        print(f"Connection from {address} has been established.")
        return clientsocket, address

    def send_reply(self, clientsocket):
        clientsocket.send(bytes("Hey there!!!", "utf-8"))
        time.sleep(3)
