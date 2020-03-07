import socket
import asyncio
from client import Requester
from server import Replier


class Communicator:
    """Send and receive json messages"""
    def __init__(self, IP, requester: Requester, replier: Replier):
        self.hosts = []
        self.IP = IP
        self.requester = requester
        self.replier = replier
        self.keep_going = True
        self.outgoing_connections = {}

    def x(self):
        """When someone connects to your replier, add their IP to
        your hosts list"""

    def y(self):
        """Send greeting to all the hosts you know about"""

    def setup(self):
        self.replier.connect((self.IP, 4321))
        
        for host in self.hosts:
            self.outgoing_connections[host] = self.requester.connect((host, 1234))

    async def handle_incoming(self):
        """"""
        clientsocket, address =  await self.replier.accept_request()
        self.replier.send_reply(clientsocket)

    async def handle_outgoing(self):
        """"""
        


async def main():
    """"""
    connect_to_IP = input('IP to connect to: ')
    comm = Communicator(socket.gethostname(), Requester(), Replier())
    comm.hosts.append(connect_to_IP)
    comm.setup()
    while comm.keep_going:
        await comm.handle_incoming()
        await comm.handle_outgoing()


if __name__ == '__main__':
    asyncio.run(main())
