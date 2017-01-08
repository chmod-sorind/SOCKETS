import socket
import threading
from queue import Queue


print_lock = threading.Lock()
server = 'localhost'


def portScan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = sock.connect((server, port))
        with print_lock:
            print('port', port, 'is open')
        connection.close()
    except:
        pass


def threader():
    while True:
        Worker = q.get()
        portScan(Worker)
        q.task_done()

q = Queue()

for x in range(600):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

for worker in range(1, 65535):
    q.put(worker)
q.join()
