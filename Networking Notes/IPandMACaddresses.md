# IP and MAC Addresses

### How to find your local IP address:
* On Windows: ```ipconfig```
* On Linux:
	* ```hostname -I```
	* or ```ifconfig``` 
		* next to ```inet```

### IP Addresses, IPv4 vs IPv6
In IPv4, each number set around the periods represent 8 bits. For example, in the address 192.168.232.133, the first number set ```192``` can be represented in 8 bits: ```1100 0000```, and the next set of numbers ```168``` can be represented in 8 bits as well: ```1010 1000```... and so on. (A smaller number such as 8 can be represented with 0's on the left hand side as that doesn't affect the number).


This means that the maximum "number" each set can be is 255, because 256 is represented by 9 bits (1 0000 0000).


The number of possibilities for IPv4 addresses can be calculated by doing 2^32 = about 4.295 million... This is not enough...


To solve this, NAT (Network Address Translation) is used. From [Cisco's website](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/26704-nat-faq-00.html#:~:text=A.,designed%20for%20IP%20address%20conservation.&text=NAT%20operates%20on%20a%20router,are%20forwarded%20to%20another%20network.) ```It enables private IP networks that use unregistered IP addresses to connect to the Internet. NAT operates on a router... Basically, NAT allows a single device, such as a router, to act as an agent between the Internet (or public network) and a local network (or private network), which means that only a single unique IP address is required to represent an entire group of computers to anything outside their network.```


Basically NAT (usually on a router) converts the private/local IP addresses (such as ```192.168.234.122```) on your devices to your actual assigned IP (by your internet service provider, can be something like ```25.12.21.2```) so that it can traverse the web as a real IP address. 


Private IP addresses are addresses that cannot traverse the web, they are local to your own network until it's converted by a NAT to communicate online. Below is a graphic showing the list of private IP addresses:

![image](https://user-images.githubusercontent.com/41026969/87213809-a0df8280-c2f5-11ea-8184-c1b8e6534e1c.png)


IPv6 is different, it's represented as 8 groups, of 4 hex digits, so to calculate the number of possible IPv6 addresses is 2^128 which is a very large number... Though because of NAT, using IPv6 isn't common.

![image](https://user-images.githubusercontent.com/41026969/87213935-ad180f80-c2f6-11ea-889f-04bbfdbf1742.png)


### MAC addresses
* Stands for Media Access Control
* It is a devices physical adddress
* Helps switches/routers identify each device on the network
* First 3 pairs of the MAC address identifies what type of device, these set of numbers are also known as identifiers.