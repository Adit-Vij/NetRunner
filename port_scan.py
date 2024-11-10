import socket
import threading

HOST = '127.0.0.1'
NUM_THREADS = 4

def scan_ports_range(start,end,open_ports):
    for port in range(start,end+1):

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.25)
        result = sock.connect_ex((HOST, port))

        if result == 0:
            open_ports.append(port)
            sock.close()


def scan_ports(start,end):

    open_ports = []
    thread_list = []
    range_size = (end - start + 1) // NUM_THREADS

    for i in range(NUM_THREADS):

        range_start = start + i*range_size
        range_end = start + (i + 1) * range_size - 1 if i != NUM_THREADS - 1 else end
        thread = threading.Thread(target=scan_ports_range, args=(range_start,range_end,open_ports))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()
    return open_ports #Global List