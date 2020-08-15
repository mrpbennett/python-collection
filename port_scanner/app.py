import os
import socket
import threading
from queue import Queue

from dotenv import load_dotenv

load_dotenv()

target = os.getenv("TARGET")
queue = Queue()
open_ports = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port is {port} is open!")
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(500):
    threat = threading.Thread(target=worker)
    thread_list.append(threat)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)

