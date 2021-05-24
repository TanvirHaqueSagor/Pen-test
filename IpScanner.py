#!/bin/python3

import sys #command line argument 
import socket
from datetime import datetime

#define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #host name to IPv4
else:
	print("Invalide argument")
	print("Syntacx: python3 scanner.py <ip>")
	sys.exit()

#banner
print("-" * 50)
print("Scanning target "+ target)
print("Started time "+ str(datetime.now()))
print("-" * 50)

try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		result = s.connect_ex((target,port)) #return error indicator
		print("Checking the port{}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
