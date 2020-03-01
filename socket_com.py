import socket

self_ip = ''
host_list = ['192.168.1.86', '192.168.176']


def get_Host_name_IP():
    global self_ip
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
    except Exception:
        print("Unable to get Hostname and IP")


get_Host_name_IP()