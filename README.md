# Seg Scanner
Seg Scanner is a python package made to help with segmentation scanning during network security assessments. It scans a list of ports in an IP range and returns a list of open ports.

## An Overview of Seg Scanner
Seg-scanner (short for segmentation scanner) checks to make sure that a computer in one subnet cannot reach a computer in another. Many cyber security compliacne criteria require that network segementation be put in place. For example PCI DSS requires that systems which stores, processes or transmit credit card data are isolated from those that do not. Segmentation scanning confirms that a computer on a certain subnet cannot reach another by attempting to connect to all ports of the corresponding subnet. If no ports are accessible the network can be seen as properly segmented. This seg scanner can be used in the flowing scenarios:
- Ethical hacking & Red Teaming
- Confirming Security Policy Implementation
- Confirming that Zero Trust has been correctly implemented
- Confirming that micro-segmentation has been correctly implemented

For more info on the use-cases of network segemntation watch the video below.
[![Watch the video](https://img.youtube.com/vi/ouvqTP3RajU/maxresdefault.jpg)](https://youtu.be/ouvqTP3RajU)

### Additional Technical Details
The seg-scanner package is a thread safe port scanner that takes an IP range, and a list of ports. It opens a socket and attempts to connect to every port in the list of ports for each IP in the IP range. It returns a list of open ports to standard output. Because this package is thread-safe and asyncronus multiple seg-scanners can be ran asyncronusly. The seg-scanner package takes an optional argument where users can define the listening port, in the event that we are using multiple scanners simultaneously and may want to listen on seperate ports. 

## Install Instructions
- Simple for the end user
- Documentation
- Non Technical

## Contribution Guidelines
- Technical
- For Programers
 
## Expectations for developers
- Fill out template 
- Squash merges
- IDK

## Known Issues
- Project incomplete
- Readme needs work

## Donation Link
- Non existent at the moment