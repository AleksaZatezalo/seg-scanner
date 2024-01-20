"""
Description: A multi-threaded and async scanner intended to enumerate open ports on a subnet.
Version: 1.0.0
Date (Last Updated): January 2024
Original Author: Aleksa Zatezalo
"""

from segScanner import segScanner
import asyncio
import time    

seg = segScanner("31.13.80.36", "80")
asyncio.run(seg.scanIPRange())
time.sleep(10)
print(seg.output)