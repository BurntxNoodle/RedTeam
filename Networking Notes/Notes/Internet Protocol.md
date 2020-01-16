# Internet Protocol

### Example of ethernet communication:

From the client to the server:

1) Ethernet
2) Ethernet Payload which contains:
	- IP: contains source/destination IP, source/destination port, and type of data (HTTP data, VoIP data, etc.)
	- Type of protocol (TCP or UDP; for this example let's say it'll be TCP)
	- The TCP (or UDP) payload: if it's TCP, a TCP payload an example could be something like HTTP data
3) Server

So the HTTP data is packaged within TCP, which is packaged in IP which is packaged into Ethernet.

### TCP and UDP

- Both of these are different ways to move data 
- It is OSI Model Layer 4: the transport layer
- Allows use of multiple applications at the same time over the network (multiplexing)
- Some applications use TCP, some use UDP

Picture of the OSI layers:
![image](https://user-images.githubusercontent.com/41026969/72492131-23293700-37ea-11ea-89f2-a609f9bf4eb6.png)

### TCP
- Transmission Control Protocol
- Data is transferred from user to server, then terminated. 
- "reliable" delivery as it can get recovery from errors 
- expects communication back that something is received successfully (like a 'read' receipt)
- Receiving device can manage how much data is sent, this is called Flow control

### UDP
- User Datagram Protocol   
- No formal call setup or breakdown process, thus it is considered "connectionless"
- "unreliable" delivery, no return receipt. No verification that data was receieved 
- Primarily to send data

### Addresses
- Transferring data from one IP address to another IP address
- In the data, there is a port number to determine where in the IP address it will be going to
- Each port usually has a designated service/applications
- Port 80 is usually web traffic
- Port 443 is encrypted web traffic
- Port 25 is usually mail service

### Ports
- IPv4 sockets: server IP addresses, protocol, server application port number. or client IP address, protocl, client port number
- two types of port groups: Non ephemeral and ephemeral 
- Non ephemeral ports are parmenent port numbers like ports 0 - 1023, usually on a server or service.
- Ephemeral ports: temporary port numbers that are not for permanent use: usually ports 1024 - 65535 which are determined in real-time by the client.
- TCP/UDP can be between 0-65535
- Most servers and services uses non-ephemeral port number. 
- Service port numbers need to be well known so that accessing it is facilitated. 
- TCP port numbers aren't the same as UDP port numbers (TCP port 80 does NOT conflict with UDP port 80)
- In the example above (at the start): the client will use TCP port 80 to send HTTP 

Here's a graphic to break it down:

![image](https://user-images.githubusercontent.com/41026969/72492164-40f69c00-37ea-11ea-8161-87e8ca1667e3.png)

### ICMP 
- Internet Control Message Protocol
- Protocol carried by IP
- Usually done by administrators to check if machine is running (thus an ICMP request will be sent and an ICMP response will be received it is running)
- If a service is down an ICMP response will be sent, and since the server/service/network is down or isn't responsive, an ICMP response will tell the administrator it has not been able to communicate with the network.
