# Seg Scanner
Seg Scanner is a python package made to help with segmentation scanning during network security assessments. It scans a list of ports in an IP range and returns a list of open ports.

## An Overview of Seg Scanner
Seg-scanner (short for segmentation scanner) checks to make sure that a computer in one subnet cannot reach a computer in another. It is made quickly scan a list of IPs and a corresponsing ports. Many cyber security compliacne criteria require that network segementation be implemented. For example PCI DSS requires that systems which stores, processes or transmit credit card data are isolated from those that do not. Segmentation scanning confirms that a computer on a certain subnet cannot reach another by attempting to connect to all ports of the corresponding subnet. If no ports are accessible the network can be seen as properly segmented. This seg scanner can be used in the flowing scenarios:
* Ethical hacking & Red Teaming
* Confirming Security Policy Implementation
* Confirming that Zero Trust has been correctly implemented
* Confirming that micro-segmentation has been correctly implemented
* Compliance

For more info on the use-cases of network segemntation watch the video below.
[![Watch the video](https://img.youtube.com/vi/ouvqTP3RajU/maxresdefault.jpg)](https://youtu.be/ouvqTP3RajU)

### Additional Technical Details
The seg-scanner package is an asyncronus and thread port scanner that takes an IP range, and a list of ports. It opens a socket and attempts to connect to every port in the list of ports for each IP in the IP range. It returns a list of open ports to standard output. A request to a specific port on a specific IP is made asyncronusly. When scanning a subnet, multiple threads are spawned with each thread making asyncronus reguests for a corresponding IP. This package is made to support both UDP and TCP port scanning.

More details on port scanning and it's inner workings along with an in-depth description for the diagram below can be found [here](https://www.paloaltonetworks.com/cyberpedia/what-is-a-port-scan). 

<p align="center">
    <img src="port-scanning-attack.webp" />
</p>

## Why Not Nmap?
* Fill This Out (Important)
* Debatibly Faster (Look Into Threading And Asyncio for NMAP)
* Disscuss Pasuing Functionality and Rate Limiting

## Install Instructions
Install instructions are pending package release.

## Contribution Guidelines
When contributing to this repository, please first discuss the change you wish to make via issue here on GitHub. Make sure all pull requests are tagged with a specific ticket number found in the repositories issues section.Before making any changes please create your own branch. Follow all three points below before opening a PR:
1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2.  Make sure all corresponding test cases pass.
3. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.

Note that we have a code of conduct. Follow it in all your interactions with the project.

## Known Issues
A list of known issues and features that are currently in development will be maintained here. Please open an issue in github if you would like something addressed.

## Donation Link
If you have benefited from this project and use Monero please consider donanting to the following address:
46NzxHXUwe4UEJjNE6aebo8gz4D8KaBr3iq9bLdStspNaY1xaWxGtzA1pCbooRA4keXphzkY3326ZC9wHGTMTStJ8NPWXzZ