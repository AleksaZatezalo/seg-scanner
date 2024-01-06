# Seg Scanner
Seg Scanner is a python package made to help with segmentation scanning during network security assessments. It takes a range of IPs, a range of ports, and a daily time range within which it can run. It will run every day in that time range untill the range of ports on every IP in the IP range has scanned. Apon compleation it will return a list of open ports.

## What is Segmentation Scanning?
Many cyber security compliacne criteria such as PCI DSS require that systems which stores, processes or transmit credit card data are isolated from those that do not.