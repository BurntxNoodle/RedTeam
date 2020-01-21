# HackTheBox Shocker

### Enumeration 

Starting of with a standard enumeration scan: ```nmap -sC -sV -oA shocker 10.10.10.56```. Bellow is the output:

![image](https://user-images.githubusercontent.com/41026969/72769401-8d662100-3bc8-11ea-91a9-1633f24b6da5.png)

Port 80 which is used for HTTP is open to us. Checking out what the main page is to see if there's any clues:

![image](https://user-images.githubusercontent.com/41026969/72771202-23507a80-3bce-11ea-8efd-7463d2184f81.png)

We see that the home page is just an image. Next, I decide to enumerate to see if there's any interesting directories. 

The first tools I use is ```gobuster``` which is a CLI tool to bruteforce the websites files/directories. Here are the results:

![image](https://user-images.githubusercontent.com/41026969/72770980-7bd34800-3bcd-11ea-95a8-30e3ce733307.png)

Since gobuster didn't pick anything up, I decide to use dirbuster, which is a similar tool excepted it has a graphical interace to see if it picks up anything. Here are the settings that I used:

![image](https://user-images.githubusercontent.com/41026969/72772490-0b7af580-3bd2-11ea-8b11-6b01c06a3bad.png)

Here's what dirbuster finds:

![image](https://user-images.githubusercontent.com/41026969/72773203-5f86d980-3bd4-11ea-83ac-a88d269447a5.png)
