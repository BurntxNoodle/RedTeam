# The OSI Model

The OSI model (Open Systems Interconnection Model) is a model that splits up networking communication into a system of seven layers. Picture of the different layers below by [Cloudfare](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/):

![image](https://user-images.githubusercontent.com/41026969/87237758-eff5e800-c3c7-11ea-8e12-8668325e09e5.png)

Information on each of the layers starting from the bottom:

* Physical 
	* Responsible for physical transmission and reception to a device.
	* It converts digital bits into electrical, radio, or optical signals.
	* Includes things like Bluetooth, Ethernet, and USB.
* Datalink 
	* Defines the protocol to use during the establishment/termination of a connection. Also defines the protocol for flow control between them.
	* Most switches operate at level 2
	* Provides node-to-node data transfer, creating a link between the connected nodes
	* Detects and possibly corrects errors that may occur in the physical layer
* Network
	* IP address
	* Router funtionality
	* Responsible for packet forwarding, including routing through different routers
* Transport
	* TCP/UDP port numbers work at layer 4
	* Coordination of data transfers between client/host
	* Information such as how much data to send, at what rate, where it goes, etc.
* Session
	* Setting up the coordination of connection/termination between applications
	* Session Management
* Presentation
	* Prepares data so that it can be used by the application layer
	* Translation, encryption, and compression of data
	* MOV, JPEG, WMV
* Application
	* HTTP, SMTP
	* What most users see - "closest to the end user"
	* Applications that work at Layer 7 are the ones that users interact with directly such as web browser, mail, skype, etc. 