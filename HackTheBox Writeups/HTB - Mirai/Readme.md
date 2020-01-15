# HackTheBox - Mirai

Note: This box is more of a forensics type challenge, never had any prior experience to forensics except for reverse engineering challenges in CTFs so this was pretty interesting to me.

[Sources](https://github.com/BurntxNoodle/RedTeam/tree/master/HackTheBox%20Writeups/HTB%20-%20Mirai#Sources)

### Enumeration 

To start off, I do: ```nmap -sC -sV -oA mirai 10.10.10.48```. Here's what was outputted:

![image](https://user-images.githubusercontent.com/41026969/72224053-fa801380-3543-11ea-9c41-f60a7712eb4a.png) 

There are a few ports open:
- Port 22 which is an SSH server. Currently we have no creds we can try.
- Port 53 which is a DNS server. Doing some research [about DNS](https://www.grc.com/port_53.htm): ```Port 53 is used by the Domain Name System (DNS), a service that turns human readable names into IP addresses that the computer understands.``` More specifically about [dnsmasq](https://en.wikipedia.org/wiki/Dnsmasq): ```Dnsmasq provides Domain Name System (DNS) forwarder, Dynamic Host Configuration Protocol (DHCP) server, router advertisement and network boot features for small computer networks, created as free software.```
- Port 80 which is a webserver.

Checking out the main page of the website: 

![image](https://user-images.githubusercontent.com/41026969/72390779-8f783d80-36f9-11ea-9893-afa87bcda2bc.png)

We can verify that the ```nmap``` scan is correct the main homepage is a blank HTML page.

Next step is to run a ```gobuster``` scan to find any potential directories: ```gobuster dir -u http://10.10.10.48 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt```. 

(Explanation of the code above): ```gobuster``` will run the application. ```dir``` is the mode that we'll be using gobuster for (it will brute force directories). ```-u``` is the flag that the next string is the URL. ```-w``` is the flag that the next string is the wordlist that we'll be using.

Here is the output of running that gobuster scan:

```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.48
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/01/08 18:25:05 Starting gobuster
===============================================================
/admin (Status: 301)
/versions (Status: 200)
===============================================================
2020/01/08 18:39:02 Finished
===============================================================
```

```gobuster``` discovered two URLs:

- ```http://10.10.10.48/admin```
- ```http://10.10.10.48/versions```

Visiting the ```/admin``` directory:

![image](https://user-images.githubusercontent.com/41026969/72391426-11b53180-36fb-11ea-987e-359606d26de5.png)

We see there's a webpage that has something called ```Pi-hole```. 

From the [Pi-hole wiki page](https://en.wikipedia.org/wiki/Pi-hole): ```Pi-hole is a Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole (and optionally a DHCP server), intended for use on a private network. It is designed for use on embedded devices with network capability, such as the Raspberry Pi, but it can be used on other machines running Linux and cloud implementations.```

So from this page, it is learned that Pi-hole does advertisement and internet tracker blocking on a private network. It is also learned that it's designed for devices like a Raspberry Pi. 

### Getting a shell

Doing some research I come across a [an article](https://itsfoss.com/ssh-into-raspberry/) with SSH info into a Raspberry Pi. It says the default credentials are 

```
user: pi
password: raspberry
```

Testing out those credentials:

![image](https://user-images.githubusercontent.com/41026969/72392352-d5370500-36fd-11ea-93b8-75e12eec85a4.png)

We get a shell.

Doing an ```id``` check reveals we aren't a root user. 

Wandering out and eventually checking out the ```Desktop``` directory, we get the user flag:

![image](https://user-images.githubusercontent.com/41026969/72393136-03b5df80-3700-11ea-9001-088f04fbb5d1.png)

Though doing a ```sudo -l``` command to list commands that are allowed on our current user. Doing so results in this:

```
pi@raspberrypi:~ $ sudo -l
Matching Defaults entries for pi on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User pi may run the following commands on localhost:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: ALL
```

This means we can run ```sudo su - ``` to switch to the ```root``` user without a password.

![image](https://user-images.githubusercontent.com/41026969/72392860-1a0f6b80-36ff-11ea-9a16-9781f0de4d5e.png)

### Flags
user: ```/home/pi/Desktop/user.txt```
root: ```See above: 


### Sources
- [Info on port 53](https://www.grc.com/port_53.htm)
- [Info on DNSmasq](https://en.wikipedia.org/wiki/Dnsmasq)
- [Pi-hole wiki](https://en.wikipedia.org/wiki/Pi-hole)
- [SSH into Raspberry Pi](https://itsfoss.com/ssh-into-raspberry/)
- [Mirai video writeup by IppSec](https://www.youtube.com/watch?v=SRmvRGUuuno)

### under construction 
