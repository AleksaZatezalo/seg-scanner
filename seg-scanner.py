"""
Description: A multi-threaded and async scanner intended to enumerate open ports on a subnet.
Version: 1.0.0
Date (Last Updated): January 2024
Original Author: Aleksa Zatezalo
"""

##### To Do List#####
# 1. Make It Threaded Across an IP Range (& Add Time)
# 2. Make It A Package
# 3. Compate it to NMAP speed for port scanning (Add to Readme)
# 4. Optimize README (Make it consise, SEO Optimized, Add New Monero)
# 5. Publish the package
# 6. Add to Hacktoberfest, Share on Discord, Share on & Share With Friends

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

        return list(ipaddress.ip_network(self.ipRange, False).hosts())

    async def test_port_number(self, host, port):
        """
        Uses async function calls to test if a TCP port is open.
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

            conn = await self.test_port_number(str(host), str(port))
            if conn:
                 # report the report if open
                 print(f'> {host}:{port} [OPEN]')
            # mark the item as processed
            task_queue.task_done()

    async def scanIPs(self, limit = 100):
        targets = self.subnetToIPs()
        for target in targets:
            print("Scanning: " + str(target))
            # create the task queue
            task_queue = asyncio.Queue()
            # start the port scanning coroutines
            workers = [asyncio.create_task(self.scanPorts(target, task_queue)) for _ in range(limit)]

            # issue tasks as fast as possible
            # for port in self.portRange:
            #     print("Adding port: " + port)
            #     # add task to scan this port
            #     await task_queue.put(port)
            # wait for all tasks to be complete
            await task_queue.put(80)
            await task_queue.join()

            # signal no further tasks
            await task_queue.put(None)
 
# define a host and ports to scan
scan = segScanner("151.101.192.223/32", "80")

asyncio.run(scan.scanIPs())