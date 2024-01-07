"""
Description: A multi-threaded and async scanner intended to enumerate open ports on a subnet.
Version: 1.0.0
Date (Last Updated): January 2024
Original Author: Aleksa Zatezalo
"""

##### To Do List#####
# 1. Make Concurent Port Scanner
# 2. Make It Asyncio
# 3. Make It Work For Subnet
# 4. Make It A Package
# 5. Test It Thourougly

# Imports
import argparse
import socket
import errno
import threading
import queue
import asyncio


#Initialize the parser
parser = argparse.ArgumentParser(description='A port scanner capable of basic TCP connect scans.')
parser.add_argument('Target', help='an ip or hostname to scan.')
parser.add_argument('-p', help='a port range specified using the \'-\' character or a comma separated list of ports to scan (Default 1-1024).')
parser.add_argument('-t', type=int, help='number of threads to use (Default 10).')
args = parser.parse_args()

#Retrieve parameter values from the parser arguments
target = args.Target

ports = range(1,1024)
if args.p != None and "-" in args.p:
    [minPort,maxPort] = [int(i) for i in args.p.split("-")]
    ports = range(minPort,maxPort+1)
elif args.p != None:
    ports = [int(i) for i in args.p.split(",")]

threads = 10
if args.t != None:
    threads = args.t

# Global Variables
results = {}
lock = threading.Lock()
q = queue.Queue()

def connect(ip, port):
    """
    Connects to port, port, on ip address, ip, and returns the ports status.
    Three potential status codes are 'Open', 'Filtered', and 'Closed'.
    """
    
    status = ""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        connection = s.connect((ip, port))
        status = "Open"
        s.close()
    
    except socket.timeout:
        status = "Filtered"

    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            status = "Closed"
        else:
            raise e
    
    return status

def worker():
    while not q.empty():
        (ip,port) = q.get()
        status = connect(ip,port)
        lock.acquire()
        results[port] = status
        lock.release()
        q.task_done()

#Prepare queue
for port in ports:
    q.put((target,port))

#Start threads
for i in range(threads):
    t = threading.Thread(target=worker)
    t.start()

print("Started a scan of " + target + "\n" + "-"*10)
q.join()

#Present the scan results
for port in ports:
    print("Port " + str(port) + " is " + results[port])