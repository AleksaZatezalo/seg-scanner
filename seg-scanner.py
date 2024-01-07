"""
Description: A multi-threaded and async scanner intended to enumerate open ports on a subnet.
Version: 1.0.0
Date (Last Updated): January 2024
Original Author: Aleksa Zatezalo
"""

##### To Do List#####
# 2. Make it a Class
# 3. Make It Asyncio
# 4. Make It Work For Subnet
# 5. Make It A Package
# 6. Test It Thourougly

# Imports
import argparse
import socket
import errno
import threading
import queue
import asyncio

class segScanner():
    def __init__(self, target, portRange, thread=10):
        self.target = target
        self.portRange = portRange
        self.thread = thread

    def splitPortRange(self):
        """Takes self.portRange that has the format XX-YY and returns two ints XX and YY. """

        pass    


#Retrieve parameter values from the parser arguments
# target = args.Target
# 
# ports = range(1,1024)
# if args.p != None and "-" in args.p:
    # [minPort,maxPort] = [int(i) for i in args.p.split("-")]
    # ports = range(minPort,maxPort+1)
# elif args.p != None:
    # ports = [int(i) for i in args.p.split(",")]
# 
# threads = 10
# if args.t != None:
    # threads = args.t
# 
# results = {}
# lock = threading.Lock()
# q = queue.Queue()
# 
# def connect(ip, port):
    # """
    # Connects to port, port, on ip address, ip, and returns the ports status.
    # Three potential status codes are 'Open', 'Filtered', and 'Closed'.
    # """
    # 
    # status = ""
    # try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.settimeout(5)
        # connection = s.connect((ip, port))
        # status = "Open"
        # s.close()
    # 
    # except socket.timeout:
        # status = "Filtered"
# 
    # except socket.error as e:
        # if e.errno == errno.ECONNREFUSED:
            # status = "Closed"
        # else:
            # raise e
    # 
    # return status
# 
# def worker():
    # while not q.empty():
        # (ip,port) = q.get()
        # status = connect(ip,port)
        # lock.acquire()
        # results[port] = status
        # lock.release()
        # q.task_done()
# 
# for port in ports:
    # q.put((target,port))
# 
# for i in range(threads):
    # t = threading.Thread(target=worker)
    # t.start()
# 
# print("Started a scan of " + target + "\n" + "-"*10)
# q.join()
# 
# for port in ports:
    # print("Port " + str(port) + " is " + results[port])