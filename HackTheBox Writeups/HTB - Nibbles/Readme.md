# HackTheBox Nibbles

### Enumeration

Starting off with a basic enumeration scan: ```nmap -sC -sV -oA nibbles 10.10.10.75```

Here's what it outputs:

![image](https://user-images.githubusercontent.com/41026969/73245301-ecec9f80-4179-11ea-96ec-ea6e22e3fd65.png)

So we see there's a ssh server and a web server being hosted on this machine. Since we don't have any creds for ssh yet, I first check out the webpage:

![image](https://user-images.githubusercontent.com/41026969/73312921-db49dd00-41f7-11ea-8c99-d5d43e258f78.png)

Checking the source (on FireFox ESR, ```CTRL``` + ```u```) we see there's a hidden directory:

```
<!-- /nibbleblog/ directory. Nothing interesting here! -->
```

Going to ```http://10.10.10.75/nibbleblog/``` to check it out shows some kind of portal:

![image](https://user-images.githubusercontent.com/41026969/73313001-13e9b680-41f8-11ea-81c8-f1be6adba61c.png)

I initially did a gobuster scan on the main homepage ```http://10.10.10.75``` and it didn't find anything. Though trying a gobuster scan on ```http://10.10.10.75/nibbleblog/``` (using the ```directory-list-2.3-medium```) outputs:

![image](https://user-images.githubusercontent.com/41026969/73313521-7c856300-41f9-11ea-89db-e960aef7edfc.png)

Looking at the ```README``` directory:

![image](https://user-images.githubusercontent.com/41026969/73313695-e7cf3500-41f9-11ea-86f7-9aa5ec46ecce.png)

We see that the web server has ```Nibbleblog version 4.0.3 codename Coffee``` installed.

Looking up vulnerabilities for this version of Nibbleblog, there are multiple articles about file uploading:

![image](https://user-images.githubusercontent.com/41026969/73314010-b99e2500-41fa-11ea-87f6-7ff607809d93.png)

We see there's a [Rapid7](https://www.rapid7.com/db/modules/exploit/multi/http/nibbleblog_file_upload) page about it. In this article, it describes the vulnerability. ```Nibbleblog contains a flaw that allows an authenticated remote attacker to execute arbitrary PHP code. This module was tested on version 4.0.3.``` Though a thing to note about this is that we need to be on an authenticated account. So we need to keep enumerating those web directories for some credentials...

Looking around I eventually end up in the ```/content/private/users.xml``` page. Checking out the page shows there's a single user ```admin```. It is also worth noting that there seems to be a firewall/blacklist system in place to guard against bruteforcers

![image](https://user-images.githubusercontent.com/41026969/73314486-020a1280-41fc-11ea-871e-3e6c62829e81.png)
