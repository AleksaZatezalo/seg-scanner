"""
Description: A multi-threaded and async scanner intended to enumerate open ports on a subnet.
Version: 1.0.0
Date (Last Updated): January 2024
Original Author: Aleksa Zatezalo
"""

##### To Do List#####
# 1. Make This Async for Each Individual IP
# 2. Make It Threaded Across an IP Range
# 3. Add UDP Port Scanning Functionality
# 4. Make It A Package
# 5. Compate it to NMAP speed for port scanning (Add to Readme)
# 6. Optimize README (Make it consise and SEO Optimized)
# 7. Publish the package
# 8. New monero donation link (I am retarded)
# 9. Add to cool hacktober fest repositories
# 10. Share with friends (Lopez Mitic, Dr. Milan, and Whatsapp chats)

# Imports
import socket
import errno
import threading
import queue
import asyncio

class segScanner():
    def __init__(self, target, portRange=None, thread=10):
        self.target = target
        self.portRange = portRange
        self.thread = thread
        self.results = {}
        self.lock = threading.Lock()
        self.q = queue.Queue()

    def splitPortRange(self):
        """
        Takes self.portRange that has the format XX-YY and returns two ints XX and YY. 
        """

        ports = range(1,65535)
        if self.portRange != None and "-" in self.portRange:
            [minPort,maxPort] = [int(i) for i in self.portRange.split("-")]
            ports = range(minPort,maxPort+1)
        elif self.portRange != None:
            ports = [int(i) for i in self.portRange.split(",")]

        self.portRange = ports
        
    def connect(self, port):
        """
        Connects to port, port, on ip address, ip, and returns the ports status.
        Three potential status codes are 'Open', 'Filtered', and 'Closed'.
        """
        status = ""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            connection = s.connect((self.target, port))
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

    def worker(self):
        while not self.q.empty():
            (self.target,port) = self.q.get()
            status = self.connect(port)
            self.lock.acquire()
            self.results[port] = status
            self.lock.release()
            self.q.task_done()

    def execute(self):
        self.splitPortRange()
        for port in self.portRange:
            self.q.put((self.target,port))
        for i in range(self.thread):
            t = threading.Thread(target=self.worker())
            t.start()
            print("Starting Thread")
        self.q.join()
        for port in self.portRange:
            print("Port " + str(port) + " is " + self.results[port])