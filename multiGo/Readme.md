# multiGo

### What is multiGo?
Automate multiple gobuster scans given a list of directories that you want to further enumerate. This script will create a directory called ```multiGo_results``` and inside that directory, multiGo will save all results in a text file that corresponds to the results.

### How to use multiGo & How to get it
SYNTAX: ```python3 multiGo.py <ADDRESS> <DIR_LIST>```

You can go into the python source file to change any flags/settings to your needs.

```multiGo``` utilizes the tool ```gobuster```. To install ```gobuster``` on kali linux simply do: 

```
noodle@kali:~$ sudo apt-get install gobuster
```

If you already have gobuster installed, simply download the [python file]() for multiGo.

Enjoy

### Example in action
This example is used on the [HackTheBox - Nibbles](https://github.com/BurntxNoodle/RedTeam/tree/master/HackTheBox%20Writeups/HTB%20-%20Nibbles) machine.

Intitially running a ```gobuster``` scan on a URL: ```gobuster dir -u http://10.10.10.75/nibbleblog -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -n -o directories.txt``` it gives a list of directories found on that URL. Cating that file:

```
noodle@kali:~/Desktop/Hacky Sack/!Pentesting/htb-nibbles$ cat directories.txt 
/admin
/plugins
/README
/languages
/content
/themes
```
Using ```multiGo``` to automatically scan all of those web directories:

![image](https://user-images.githubusercontent.com/41026969/73464662-448f3480-434d-11ea-9824-e5f63167b35d.png)

```multiGo``` then creates a directory called ```multiGo_results/``` and inside are the findings:

![image](https://user-images.githubusercontent.com/41026969/73466534-faf41900-434f-11ea-844a-9e14d8184cf5.png)

Reading the ```admin.txt``` file will output results of the ```http://10.10.10.75/nibbleblog/admin``` directory. 
