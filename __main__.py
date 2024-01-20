"""
Description: A multi-threaded and async scanner intended to enumerate open ports on a subnet.
Version: 1.0.0
Date (Last Updated): January 2024
Original Author: Aleksa Zatezalo
"""

# Imports
import threading
import ipaddress
import asyncio

class segScanner():
    """
    Asyncronus and threaded port scanner created to see which ports are accessible within subnets.
    """

    def __init__(self, ipRange, portRange, timeout=3):
        self.ipRange = ipRange
        self.portRange = portRange
        self.timeout = timeout

    def subnetToIPs(self):
        """
        Returns a list of IP addresses based on the subnet provided when initializing the class.
        """

        # Creating dictionary
        ipList = list(ipaddress.ip_network(self.ipRange, False).hosts())
        for i in range(len(ipList)):
            ipList[i] = str(ipList[i])
        self.output = dict.fromkeys(ipList, [])
        
        return list(ipaddress.ip_network(self.ipRange, False).hosts())
    
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

    async def test_port_number(self, host, port):
        """
        Uses async function calls to test if a TCP port is open.
        
        ARGUMENTS
        * host: String. IP address of the host we are connecting too.
        * port: Integer. The port we are connecting too.
        """
        
        # create coroutine for opening a connection
        coro = asyncio.open_connection(host, port)
        # execute the coroutine with a timeout
        try:
            # open the connection and wait for a moment
            _,writer = await asyncio.wait_for(coro, self.timeout)
            # close connection once opened
            writer.close()
            # indicate the connection can be opened
            return True
        except asyncio.TimeoutError:
            # indicate the connection cannot be opened
            return False

    async def scanPorts(self, host, task_queue):
        """
        Scans a port and prints status to STDO. Adds open ports to the output dictionary.

        ARGUMENTS
        * host: String. IP address of the host we are connecting too.
        * task_queue: Queue. A queue of ports for the function scanPorts to connect to.
        """

        # read tasks forever
        while True:
            
            # read one task from the queue
            port = await task_queue.get()
            # check for a request to stop scanning
            if port is None:
                # add it back for the other scanners
                await task_queue.put(port)
                # stop scanning
                break
            # scan the port
            if await self.test_port_number(str(host), str(port)):
                # report the report if open
                print(f'> {host}:{port} [OPEN]')
                self.output[str(host)].append(port)
                # self.output[str(host)] = list(set(self.output[str(host)]))
            else: 
                print(f'> {host}:{port} [CLOSED]')

            # mark the item as processed
            task_queue.task_done()

    async def scanIP(self, limit=100, host="127.0.0.1"):
        """
        Scans an IP for open ports using async function calls.

        ARGUMENTS
        * host: String. IP address of the host we are connecting too.
        * limit: Integer. The maximum ammount of async coroutines we will have. Defualts to 100. 
        """

        # create the task queue
        task_queue = asyncio.Queue()
        # start the port scanning coroutines
        [asyncio.create_task(self.scanPorts(host, task_queue)) for _ in range(limit)]

        # issue tasks as fast as possible
        for port in self.portRange:
            # add task to scan this port
            await task_queue.put(port)
        # wait for all tasks to be complete
        await task_queue.join()

        # signal no further tasks
        await task_queue.put(None)
        

    async def scanIPRange(self):
        """
        Scans a range of IPs based on input added when the class was initialized. Opens a thread for each new IP.
        """

        # Functions needed to start program
        print("Scanning of targets begun \n")
        targets = self.subnetToIPs()
        self.splitPortRange()
        for ipAddress in targets:
            threading.Thread(target=asyncio.run, args={self.scanIP(host=ipAddress)}).start()
        return self.output
    

# import time
# seg = segScanner("31.13.80.36", "80")
# asyncio.run(seg.scanIPRange())
# time.sleep(10)
# print(seg.output)