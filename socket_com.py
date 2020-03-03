import socket
import utils
import sys

self_ip = utils.get_host_ip()
host_list = ['192.168.1.86', '192.168.176', '10.220.4.67']
print(self_ip)


MODE = sys.argv[1]

if MODE == 's':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes("Hey there!!!","utf-8"))

elif MODE == 'c':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.176', 1234))
    msg = s.recv(1024)
    print(msg.decode("utf-8"))

