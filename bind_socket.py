import socket
import sys

host = ''
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((host, port))
except socket.errno as e:
    print(str(e))

sock.listen(5)
conn, addr = sock.accept()
print('Connected to ' + addr[0] + ':' + str(addr[1]))