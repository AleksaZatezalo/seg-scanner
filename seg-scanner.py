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
# 4. Add Pausing Functionality
# 5. Make It A Package
# 6. Compate it to NMAP speed for port scanning (Add to Readme)
# 7. Optimize README (Make it consise and SEO Optimized)
# 8. Publish the package
# 9. New monero donation link (I am retarded)
# 10. Add to cool hacktober fest repositories
# 11. Share with friends (Lopez Mitic, Dr. Milan, and Whatsapp chats)

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

    async def test_port_number(self, port, timeout=3):
        # create async coroutine for opening a connection
        coro = asyncio.open_connection(self.target, port)

        # execute the coroutine with a timeout
        try:
            _, writer = await asyncio.wait_for(coro, timeout)
            # close connection once opened
            writer.close()
            # indicate that a connection can be opened
            return True
        except asyncio.TimeoutError:
            # indicate that a connection cannot be opened
            return False
        
    async def scan(self):
        # report a status message
        print("Scanning a host")

        # scan ports sequentially
        for port in self.portRange:
            if await self.test_port_number(self.target, port):
                print("Port " + port + " open")

if __name__ == '__main__':
    seg = segScanner('python.org', '79-82')
    asyncio.run(seg.scan())        
    # def connect(self, port):
    #     """
    #     Connects to port, port, on ip address, ip, and returns the ports status.
    #     Three potential status codes are 'Open', 'Filtered', and 'Closed'.
    #     """
    #     status = ""
    #     try:
    #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         s.settimeout(5)
    #         connection = s.connect((self.target, port))
    #         status = "Open"
    #         s.close()
        
    #     except socket.timeout:
    #         status = "Filtered"

    #     except socket.error as e:
    #         if e.errno == errno.ECONNREFUSED:
    #             status = "Closed"
    #         else:
    #             raise e
        
    #     return status

    # def worker(self):
    #     while not self.q.empty():
    #         (self.target,port) = self.q.get()
    #         status = self.connect(port)
    #         self.lock.acquire()
    #         self.results[port] = status
    #         self.lock.release()
    #         self.q.task_done()

    # def execute(self):
    #     self.splitPortRange()
    #     for port in self.portRange:
    #         self.q.put((self.target,port))
    #     for i in range(self.thread):
    #         t = threading.Thread(target=self.worker())
    #         t.start()
    #         print("Starting Thread")
    #     self.q.join()
    #     for port in self.portRange:
    #         print("Port " + str(port) + " is " + self.results[port])