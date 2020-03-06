import socket
import utils
import sys
import yaml

with open("config.yaml", "rb") as fh:
    config = yaml.load(fh.read())

self_ip = utils.get_host_ip()
host_list = config["hosts"]
print(self_ip)
print(host_list)

try:
    MODE = sys.argv[1]
except Exception:
    MODE = "s"

if MODE == "s":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        while True:
            clientsocket.send(bytes("Hey there!!!", "utf-8"))
            import time
            time.sleep(3)

elif MODE == "c":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.176", 1234))
    while True:
        msg = s.recv(1024)
        print(msg.decode("utf-8"))

