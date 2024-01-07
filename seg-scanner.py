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