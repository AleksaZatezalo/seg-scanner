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
# 6. Add to Hacktoberfest & Share With Friends

# Imports
import threading
import queue
import asyncio

class segScanner():
    """
    Asyncronus and threaded port scanner created to see which ports are accessible within subnets.
    """

    def __init__():
        pass

    def subnetToIPs():
        pass

    async def test_port_number():
        pass

    async def scanPorts():
        pass

    async def scanIPs():
        pass

async def test_port_number(host, port, timeout=3):
    
    # create coroutine for opening a connection
    coro = asyncio.open_connection(host, port)
    # execute the coroutine with a timeout
    try:
        # open the connection and wait for a moment
        _,writer = await asyncio.wait_for(coro, timeout)
        # close connection once opened
        writer.close()
        # indicate the connection can be opened
        return True
    except asyncio.TimeoutError:
        # indicate the connection cannot be opened
        return False
 
# coroutine to scan ports as fast as possible
async def scanner(host, task_queue):
  
    
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
        if await test_port_number(host, port):
            # report the report if open
            print(f'> {host}:{port} [OPEN]')
        # mark the item as processed
        task_queue.task_done()
 
# main coroutine
async def main(host, ports, limit=100):
    # report a status message
    print(f'Scanning {host}...')
    # create the task queue
    task_queue = asyncio.Queue()
    # start the port scanning coroutines
    workers = [asyncio.create_task(scanner(host, task_queue)) for _ in range(limit)]
    # issue tasks as fast as possible
    for port in ports:
        # add task to scan this port
        await task_queue.put(port)
    # wait for all tasks to be complete
    await task_queue.join()
    # signal no further tasks
    await task_queue.put(None)
 
# define a host and ports to scan
# host = 'python.org'
# ports = range(79, 444)
# asyncio.run(main(host, ports))