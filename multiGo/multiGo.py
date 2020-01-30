'''
multiGo.py
by Josh (BurntxNoodle)

Usage: python3 multiGo.py ADDRESS TXTfile

This program will automatically run a gobuster scan for each of the directories listed in
the text file given. It will output findings in a txt file with the name of the diretory

Read GitHub README for more information.
'''

import os
import sys
from subprocess import call

# print these error messages if the user doesn't pass in the correct arguments
if len(sys.argv) != 3:
    print("ERROR: Incorrect arguments passed into the function")
    print("Correct syntax: python3 multiGo.py <IP/Address> <txt file of directories>")
    print("\nEXAMPLE: noodle@kali:~$ python3 multiGo.py http://10.10.10.10 directory_list.txt")
    sys.exit(1)

# You might want to change beginning_arguments or default_arguments: 
beginning_arguments = "gobuster dir -u " 
default_arguments = " -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -o " 

# Other variables that will be used 
address = sys.argv[1] # web address the user inputs
directories = sys.argv[2] # .txt file with the directories
directory_list = [] # list to hold all directories
file_name = open(directories, "r") #  opens the file containing the directories

 # appends each entry (stripping off the new line character) in the text file into the list 
for listing in file_name:
	directory_list.append(listing.rstrip("\n"))

print("\n==================================")
print("multiGo - Automated gobuster scans")
print("==================================\n")

# Printing out info to the user
print("scanning the URL: " + address)
print("text file with directory list: " + directories + "\n")
print("Storing results in: ")

for directory in directory_list:
	print("multiGo_results/" + directory[1:] + ".txt")

print("")

# Creates the results directory
call("mkdir multiGo_results", shell = "True")

# Running gobuster scans for each directory given the settings
for directory in directory_list:
	print("\n" + beginning_arguments + address + directory + default_arguments + "multiGo_results/" + directory[1:] + ".txt")
	call(beginning_arguments + address + directory + default_arguments + "multiGo_results/" + directory[1:] + ".txt", shell = "True")

print("\n===================")
print("multiGo.py finished")
print("===================\n")
