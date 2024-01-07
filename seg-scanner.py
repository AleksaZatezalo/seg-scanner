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

# set a timeout of a few seconds