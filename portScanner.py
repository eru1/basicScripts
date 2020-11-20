import socket
from queue import Queue
import threading

print("Mode 1 -> 1,1024 \nMode 2-> 1,49152 \nMode 3 -> The Most Popular Ports\nMode 4 -> User Choose")
mode = int(input("Enter Mode Number : "))
run_threads = int(input("How many threads do you want to use ? : "))
target = input("Enter target IP : ")
queue = Queue()
open_ports = []


def port_scanner(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1,1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1,49152):
            queue.put(port)
    elif mode == 3:
        special_ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in special_ports:
            queue.put(port)
    elif mode == 4:
        ports = input('Enter your ports (Seperate by blank) : ')
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if port_scanner(port):
            print("Port {} is open!" .format(port))

            open_ports.append(port)

def run_scanner(threads, mode):
    get_ports(mode)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    print("Open ports are:",open_ports)

run_scanner(run_threads,mode)
