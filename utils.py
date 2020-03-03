import socket

def get_host_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        print("Unable to get Hostname and IP")
        return ''